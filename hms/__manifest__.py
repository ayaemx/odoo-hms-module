{
    'name': 'HMS',
    'version': '3.0',
    'depends': ['base', 'mail', 'crm', 'contacts'],
    'data': [
        'security/hms_security.xml',
        'security/hms_record_rules.xml',
        'security/ir.model.access.csv',
        'views/hms_patient_views.xml',
        'views/hms_department_views.xml',
        'views/hms_doctor_views.xml',
        'views/res_partner_views.xml',
        'views/hms_menus.xml',
        'reports/hms_patient_report.xml',
    ],
    'application': True,
}
