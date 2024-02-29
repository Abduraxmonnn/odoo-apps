# Python
import time
import datetime

# Odoo
from odoo import models, fields, api


class Payment(models.Model):
    _name = 'course.payment'
    _description = 'Payment'

    check_file = fields.Binary(string='File of Check')
    price = fields.Integer(string='Price', required=True)
    notes = fields.Text(string='Description')
    payer = fields.Many2one('course.student', string='Payer (Student)', required=True)
    created_date = fields.Date(string='Created Date', default=lambda *a: time.strftime('%Y-%m-%d'))

    @api.model
    def get_last_week_context(self):
        """
        Returns a dictionary containing the start and end dates of the last week.
        """
        today = fields.Date.today()
        last_week_start = today - datetime.timedelta(days=today.weekday() + 7)
        last_week_end = last_week_start + datetime.timedelta(days=6)
        return {
            'default_last_week_start': last_week_start.strftime('%Y-%m-%d'),
            'default_last_week_end': last_week_end.strftime('%Y-%m-%d'),
        }
