# -*- coding: utf-8 -*-
{
    'name': "Partner Cuba",

    'summary': """
        Partner Cuba""",

    'author': "BSF",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hidden',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/state_data.xml',
        'views/views.xml',
    ],
}
