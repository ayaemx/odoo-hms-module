from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient', string='Related Patient')
    vat = fields.Char(required=True)  # Make Tax ID mandatory

    @api.constrains('related_patient_id')
    def _check_patient_email_unique(self):
        """Prevent linking patient with email already assigned to different customer"""
        for record in self:
            if record.related_patient_id:
                patient_email = record.related_patient_id.email
                existing_customer = self.search([
                    ('email', '=', patient_email),
                    ('id', '!=', record.id),
                    ('related_patient_id', '!=', False)
                ])
                if existing_customer:
                    raise ValidationError(
                        f"Patient with email {patient_email} is already linked to customer: {existing_customer.name}"
                    )

    def unlink(self):
        """Prevent deletion of customers linked to patients"""
        for record in self:
            if record.related_patient_id:
                raise ValidationError(
                    f"Cannot delete customer '{record.name}' because it is linked to patient '{record.related_patient_id.full_name}'"
                )
        return super().unlink()
