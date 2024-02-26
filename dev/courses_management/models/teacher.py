from odoo import models, fields, exceptions
from odoo.tools.translate import _


class CourseTeacher(models.Model):
    _name = 'course.teacher'
    _description = 'Teacher Model'

    full_name = fields.Char(string='Full Name (F.I.O)', required=True)
    experience = fields.Selection([
        ('less than 1 year', 'less_one_year'),
        ('1-3 years', 'one_three_year'),
        ('3-6 years', 'three_six_years'),
        ('more than 6 years', 'more_six_years')
    ])
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    def _check_age(self):
        if self.age < 13:
            raise exceptions.ValidationError(_("Minimum age for enrollment is 13 years."))
        elif self.age > 70:
            raise exceptions.ValidationError(_("Maximum age for enrollment is 70 years."))

    def write(self, vals):
        super(CourseTeacher, self).write(vals)
        self._check_age()
