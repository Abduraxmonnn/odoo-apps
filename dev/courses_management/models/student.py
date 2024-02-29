# Python
from datetime import datetime

# Odoo
from odoo import models, fields, exceptions, api
from odoo.tools.translate import _


class CourseStudent(models.Model):
    _name = 'course.student'
    _description = 'Student Model'

    full_name = fields.Char(string='Full name (F.I.O)', required=True)
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    course_groups_ids = fields.Many2many(comodel_name='course.group', string='Course Groups')
    payment_ids = fields.One2many('course.payment', 'student_id', string='Payments')

    @api.depends('birth_date')
    def _compute_age(self):
        today = datetime.now().date()
        for student in self:
            if student.birth_date:
                birth_date = fields.Date.from_string(student.birth_date)
                student.age = today.year - birth_date.year - (
                            (today.month, today.day) < (birth_date.month, birth_date.day))
            else:
                student.age = 0

    def _check_age(self):
        if self.age < 13:
            raise exceptions.ValidationError(_("Minimum age for enrollment is 13 years."))
        elif self.age > 70:
            raise exceptions.ValidationError(_("Maximum age for enrollment is 70 years."))

    def write(self, vals):
        super(CourseStudent, self).write(vals)
        self._check_age()
