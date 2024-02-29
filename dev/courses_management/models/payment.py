from odoo import models, fields


class Payment(models.Model):
    _name = 'course.payment'
    _description = 'Payment'

    check_file = fields.Binary(string='File of Check')
    price = fields.Integer(string='Price', required=True)
    notes = fields.Text(string='Description')
    payer = fields.Many2one('course.student', string='Payer (Student)', required=True)
