# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School',
    'summary': """School Management Software OLD""",

    'description': """Treating Schools""",

    'author': 'Abduraxmon',
    'company': '1bit',
    'website': 'https://1abduraxmon-resume.my.canva.site/',

    'version': '16.0.1.0.0',
    'category': 'Tools',
    'post_init_hook': 'craete_student',
    'depends': ['base', 'contacts', 'hr', 'account'],

    'data': [
        'security/ir.model.access.csv',
        'views/school.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}