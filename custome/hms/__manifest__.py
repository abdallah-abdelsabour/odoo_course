{
    'name': 'hms',
    'summery': 'new hms',
    'description':"""
    hospital mangement system
    """,
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hms_view.xml',
        'views/hms_department_view.xml',
        'views/hms_doctor_view.xml',
        'views/hms_log.xml',
        'reports/report.xml',
        'reports/templates.xml',
    ],
    'depends': ['base',]
}