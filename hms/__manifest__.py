{
    'name': 'HMS',
    'version': '2.0',
    'depends': ['base', 'mail', 'crm' , 'contacts'],  # Added 'crm' dependency
    'data': [
        'security/ir.model.access.csv',
        'views/hms_patient_views.xml',
        'views/hms_department_views.xml',
        'views/hms_doctor_views.xml',
        'views/res_partner_views.xml',  # NEW VIEW FILE
        'views/hms_menus.xml',
    ],
    'application': True,
}
