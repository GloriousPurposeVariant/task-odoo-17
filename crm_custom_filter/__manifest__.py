# -*- coding: utf-8 -*-
{
    'name': 'CRM Custom Filter',
    'version': '1.0.0',
    'depends': ["crm", "sale_management", "purchase"],
    'data': [
        'data/sequence.xml',
        'views/account_move_view.xml',
        'views/crm_case_tree_view.xml',
        'views/res_parnter_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'crm_custom_filter/static/src/views/**/*'
        ],
    },
    'license': "LGPL-3",
    'installable': True,
    'auto_install': False,
    'application': True,
}
