# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customer Rating',
    'version': '1.1',
    'category': 'Productivity',
    'description': """
This module allows a customer to give rating.
""",
    'depends': [
        'mail',
    ],
    'data': [
        'views/student_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'assets': {
        'mail.assets_messaging': [
            'rating/static/src/models/*.js',
        ],
        'web.assets_backend': [
            'rating/static/src/scss/rating_rating_views.scss',
            'rating/static/src/components/*/*.scss',
            'rating/static/src/components/*/*.xml',
        ],
        'web.assets_frontend': [
            'rating/static/src/scss/rating_templates.scss',
        ],
        'web.tests_assets': [
            'rating/static/tests/helpers/*.js',
        ],
    },
    'license': 'LGPL-3',
}
