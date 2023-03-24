from odoo import models, fields

class Hmsloghistory(models.Model):
    _name = 'hms.loghistory'
    _rec_name = 'description'

    description = fields.Text()
    patients_id = fields.Many2one('hms.patient')

