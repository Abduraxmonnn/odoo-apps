from odoo import models, fields, exceptions
from odoo.tools.translate import _


class CourseStudent(models.Model):
    _name = 'course.student'
    _description = 'Student Model'

    full_name = fields.Char(string='Full name (F.I.O)', required=True)
    age = fields.Integer(string='Age', compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    course_groups_ids = fields.Many2many(comodel_name='course.group', string='Course Groups')

    def _check_age(self):
        if self.age < 13:
            raise exceptions.ValidationError(_("Minimum age for enrollment is 13 years."))
        elif self.age > 70:
            raise exceptions.ValidationError(_("Maximum age for enrollment is 70 years."))

    def write(self, vals):
        super(CourseStudent, self).write(vals)
        self._check_age()
