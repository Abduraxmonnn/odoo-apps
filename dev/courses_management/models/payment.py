# Python
import time
from datetime import timedelta

# Odoo
from odoo import models, fields, api


class Payment(models.Model):
    _name = 'course.payment'
    _description = 'Payment'

    check_file = fields.Binary(string='File of Check')
    price = fields.Integer(string='Price', required=True)
    notes = fields.Text(string='Description')
    created_date = fields.Date(string='Created Date', default=lambda *a: time.strftime('%Y-%m-%d'))

    student_id = fields.Many2one('course.student', string='Student')

    @api.model
    def get_last_week_context(self):
        today = fields.Date.today()
        last_week_start = today - timedelta(days=today.weekday() + 7)
        last_week_end = last_week_start + timedelta(days=6)
        return last_week_start, last_week_end
