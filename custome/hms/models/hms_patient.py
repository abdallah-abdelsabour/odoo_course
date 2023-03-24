from odoo import models, fields, api
from datetime import date
import re
from odoo.exceptions import ValidationError
class HmsPatient(models.Model):
    _name = 'hms.patient'
    _sql_constraints = [
        ('email_unique_constrain', 'UNIQUE(email)', 'This email is already exist')
    ]
    _rec_name = 'First_name'

    First_name = fields.Char()
    Last_name = fields.Char()
    Birth_date = fields.Date()
    History = fields.Html()
    CR_ratio = fields.Float()
    Blood_Type = fields.Selection([
        ('A', 'A',),
        ('B', 'B',),
        ('AB', 'AB',),
        ('O', 'O',),
    ])
    state = fields.Selection([
        ('undetermined', 'Undetermined',),
        ('good,', 'Good,',),
        ('fair,', 'Fair,',),
        ('serious', 'Serious',),
    ])
    PCR = fields.Boolean()
    image = fields.Image()
    Address = fields.Text()
    Age = fields.Integer(compute='_birth_onchange')
    department_id = fields.Many2one('hms.department')
    doctor_id = fields.Many2many('hms.doctor') # many to many & one to many  'ids'
    log_id = fields.One2many('hms.loghistory', 'patients_id')
    Capacity = fields.Integer(related='department_id.Capacity')
    email = fields.Char()

    @api.onchange('Age')
    def _age_onchange(self):
        if self.Age<30 and self.Age != 0:
            self.PCR = True
            return {'warning': {'title': 'PCR Message', 'message': 'PCR IS CHECKED'}}
        else:
            self.PCR = False

    @api.onchange('Birth_date')
    def _birth_onchange(self):
        for record in self:
            if record.Birth_date:
                record.Age = date.today().year - record.Birth_date.year
            else:
                record.Age = 0

    def serious(self):
        self.state = 'serious'

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')

    def write(self, vals):
        if 'state' in vals:
            self.env['hms.loghistory'].create({'description': 'State changed to NEW_STATE',
                                            'patients_id': self.id})
        super().write(vals)
