from odoo import models, fields


class Doctor(models.Model):
    _name = 'hms.doctors'
    # _rec_name = 'last_name'

    First_name = fields.Char(size=100, string="First Name")
    Last_name = fields.Char(size=100, string="Last Name")
    image = fields.Image()
