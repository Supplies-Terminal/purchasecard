# -*- coding: utf-8 -*-
{
    'name': "ST Purchasecard",

    'summary': """
        Print purchasecard for ST""",

    'description': """ 
    """,

    'author': "alvin.z",
    'website': "https://suppliesterminal.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
