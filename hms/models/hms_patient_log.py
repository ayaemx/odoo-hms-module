from odoo import models, fields

class HmsPatientLog(models.Model):
    _name = 'hms.patient.log'
    _description = 'Patient Log History'
    _order = 'date desc'

    patient_id = fields.Many2one('hms.patient', required=True, ondelete='cascade')
    created_by = fields.Many2one('res.users', required=True, default=lambda self: self.env.user)
    date = fields.Datetime(required=True, default=fields.Datetime.now)
    description = fields.Text(required=True)

