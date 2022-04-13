from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"

    is_instructor = fields.Boolean(string="Instructor")
    last_name = fields.Char(string="Last Name")
    first_name = fields.Char(string="First Name")
    middle_name = fields.Char(string="Middle Name")
    full_name = fields.Char(string="Full Name")

    age = fields.Integer(string="Age")

    @api.onchange('last_name','middle_name','first_name')
    def onchange_names(self):
        for rec in self:
            rec.full_name = "%s %s %s" %(rec.first_name, rec.middle_name, rec.last_name)

    @api.constrains('age')
    def _check_something(self):
        for record in self:
            if record.age < 18:
                raise ValidationError("Age is less than 18")
