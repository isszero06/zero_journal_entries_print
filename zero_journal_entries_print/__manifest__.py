# -*- encoding: UTF-8 -*-
{
    'name': 'Print Journal Entries (PDF)',
    'version': '6.1.0',
        "author": 'Zero Systems',
        "company": 'Zero for Information Systems',
         "website": "https://erpzero.com",
        "email": "sales@erpzero.com",
    'category': 'Accounting',
    'sequence': 1,
    'summary': 'Print Journal Entries PDF',
    'description': """
    this module use for print journal Entries in PDF report"
    """,
    'depends': ['account'],
    'data': [
        'report/report.xml'
    ],
    "price": 10.00,
    "currency": 'EUR',
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    "application": True,
    'pre_init_check_vers': 'pre_init_check_vers',
    'images': ['static/description/logo.PNG'],
}
