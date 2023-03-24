from odoo import models, fields, api
from odoo.exceptions import UserError

class CrmInhirt(models.Model):
    _inherit = 'res.partner'
    related_patient_id = fields.Many2one('hms.patient')

    @api.constrains('related_patient_id')
    def valid_email(self):
        if self.email == self.related_patient_id.email:
            raise UserError('Email not validation')

    def unlink(self):
        if self.related_patient_id:
            raise UserError('Customer linked with patient')
        return super().unlink()

