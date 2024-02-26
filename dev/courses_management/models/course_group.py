from odoo import models, fields


class CourseGroup(models.Model):
    _name = 'course.group'
    _description = 'Course Group Model'

    name = fields.Char(string='Name', required=True)
    teacher_ids = fields.Many2many('course.teacher', string='Teachers')
    course_ids = fields.Many2many('course', string='Courses', required=True)
