from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HmsDepartment(models.Model):
    _name = 'hms.department'
    _description = 'Hospital Department'
    _rec_name = 'name'

    name = fields.Char(required=True)
    capacity = fields.Integer(required=True)
    is_opened = fields.Boolean(default=True)
    patient_ids = fields.One2many('hms.patient', 'department_id', string='Patients')
    doctor_ids = fields.Many2many('hms.doctor', string='Doctors')
    patient_count = fields.Integer(compute='_compute_patient_count')

    @api.depends('patient_ids')
    def _compute_patient_count(self):
        for rec in self:
            rec.patient_count = len(rec.patient_ids)

    @api.constrains('capacity', 'patient_count')
    def _check_capacity(self):
        for rec in self:
            if rec.patient_count > rec.capacity:
                raise ValidationError("Department capacity exceeded!")
