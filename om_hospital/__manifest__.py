{
    'name': 'Hospital Management System',
    'version': '17.0.1.0.0',
    'summary': 'Manage patients, appointments and billing in Odoo 17',
    'description': """
Hospital Management System for Odoo 17
======================================
Patient records, appointments with a status workflow, appointment lines with
products, invoice integration, role-based menus and email confirmations.
""",
    'author': 'Sammer',
    'category': 'Services',
    'depends': ['base', 'mail', 'product', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/email_template.xml',
        'views/patients_views.xml',
        'views/patients_readonly_views.xml',
        'views/patients_tag_views.xml',
        'views/appointment_lines_views.xml',
        'views/appointments_views.xml',
        'views/account_move_views.xml',
        'views/patient_complaint_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
