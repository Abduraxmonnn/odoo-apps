from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _description = 'Course Model'

    name = fields.Char(string='Name', required=True)
    duration = fields.Integer(string='Duration')
    price = fields.Integer(string='Price', required=True)
    notes = fields.Text(string='Notes')
