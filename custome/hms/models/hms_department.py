from odoo import models,fields

class Hmsdepartment(models.Model):
    _name = 'hms.department'

    name = fields.Char()
    Capacity = fields.Integer()
    is_opened = fields.Boolean()
    Patients = fields.One2many('hms.patient', 'department_id')
