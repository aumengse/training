from odoo import models, fields

class Course(models.Model):
    _name = 'course'
    _description = "Course Model"

    name = fields.Char(string="Name", required=1)
    description = fields.Text(string="Course Description")
    active = fields.Boolean(string="Active",default=True)
    responsible_id = fields.Many2one('res.users', string="Responsible", default= lambda self: self.env.uid)
    instructor_ids = fields.Many2many('res.partner', string="Instructors")
    session_ids = fields.One2many('session','course_id',string="Sessions")