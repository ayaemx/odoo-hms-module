from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError
import re

class HmsPatient(models.Model):
    _name = 'hms.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    _rec_name = 'full_name'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    full_name = fields.Char(compute='_compute_full_name', store=True)
    email = fields.Char(string='Email', required=True)  # NEW FIELD
    birth_date = fields.Date(required=True)
    age = fields.Integer(compute='_compute_age', store=True)
    blood_type = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')
    ], required=True)
    pcr_test = fields.Boolean()
    cr_ratio = fields.Float()
    history = fields.Html()
    image = fields.Binary()
    address = fields.Text()
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')
    ], default='undetermined', tracking=True)
    department_id = fields.Many2one('hms.department', string='Department')
    department_capacity = fields.Integer(related='department_id.capacity', readonly=True)
    doctor_ids = fields.Many2many('hms.doctor', string='Doctors')
    log_history_ids = fields.One2many('hms.patient.log', 'patient_id', string='Log History')

    _sql_constraints = [
        ('unique_email', 'unique(email)', 'Email address must be unique!')
    ]

    @api.constrains('email')
    def _check_valid_email(self):
        """Validate email format"""
        for record in self:
            if record.email:
                email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(email_pattern, record.email):
                    raise ValidationError("Please enter a valid email address.")

    # ... (keep all your existing methods unchanged)
    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for rec in self:
            rec.full_name = f"{rec.first_name} {rec.last_name}" if rec.first_name and rec.last_name else ""

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - ((today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else:
                rec.age = 0

    @api.constrains('department_id')
    def _check_department_open(self):
        for rec in self:
            if rec.department_id and not rec.department_id.is_opened:
                raise ValidationError("Cannot assign patient to a closed department.")

    @api.constrains('cr_ratio', 'pcr_test')
    def _check_cr_ratio_required(self):
        for rec in self:
            if rec.pcr_test and not rec.cr_ratio:
                raise ValidationError("CR Ratio is required when PCR is checked.")

    @api.onchange('age')
    def _onchange_age(self):
        if self.age and self.age < 30:
            self.pcr_test = True
            return {
                'warning': {
                    'title': 'PCR Test Auto-Checked',
                    'message': 'PCR test has been automatically checked for patients under 30.'
                }
            }

    @api.onchange('pcr_test')
    def _onchange_pcr_test(self):
        if self.pcr_test and not self.cr_ratio:
            return {
                'warning': {
                    'title': 'CR Ratio Required',
                    'message': 'CR Ratio field is mandatory when PCR test is positive.'
                }
            }

    def action_set_good(self):
        for rec in self:
            rec.state = 'good'

    def action_set_fair(self):
        for rec in self:
            rec.state = 'fair'

    def action_set_serious(self):
        for rec in self:
            rec.state = 'serious'

    def action_set_undetermined(self):
        for rec in self:
            rec.state = 'undetermined'

    def write(self, vals):
        for rec in self:
            old_state = rec.state
            result = super().write(vals)
            if 'state' in vals and vals['state'] != old_state:
                rec.env['hms.patient.log'].create({
                    'patient_id': rec.id,
                    'description': f"State changed to {vals['state']}",
                    'created_by': rec.env.user.id,
                    'date': fields.Datetime.now(),
                })
            return result
