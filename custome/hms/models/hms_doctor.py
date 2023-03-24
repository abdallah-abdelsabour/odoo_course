from odoo import models,fields

class Hmsdoctor(models.Model):
    _name = 'hms.doctor'
    _rec_name = 'First_name'

    First_name = fields.Char()
    Last_name = fields.Char()
    image = fields.Image()