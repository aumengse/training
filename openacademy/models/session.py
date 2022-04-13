from odoo import models, fields, api

class Session(models.Model):
    _name = 'session'
    _description = "Session Model"

    name = fields.Char(string="Name")
    display_name = fields.Char(string="Display Name", compute='compute_display_name', store=True)
    start_date = fields.Date(string="Date")
    active = fields.Boolean(string="Active",default=True)
    duration = fields.Float(string="Duration")
    number_seat = fields.Integer(string="Number of Seats", default=10)
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('course', string="Course")
    attendee_ids = fields.Many2many('res.partner','session_partner_rel', string="Attendees")

    @api.depends('name','instructor_id')
    def compute_display_name(self):
        for rec in self:
            rec.display_name = "%s - %s" %(rec.name,rec.instructor_id.name)


