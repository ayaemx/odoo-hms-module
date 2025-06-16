from odoo import models, fields, api

class HmsDoctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Hospital Doctor'
    _rec_name = 'full_name'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    full_name = fields.Char(compute='_compute_full_name', store=True)
    image = fields.Binary()
    department_ids = fields.Many2many('hms.department', string='Departments')

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for rec in self:
            rec.full_name = f"{rec.first_name} {rec.last_name}" if rec.first_name and rec.last_name else ""
