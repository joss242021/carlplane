# -*- coding: utf-8 -*-

{
    'name': "carlplane",

    'summary': """
        Sale's Air Plane Ticked""",

    'description': """
        This Module has Created for a Sale's Air Plane Ticked to Caribbean Flight Tours Company.
    """,

    'author': "Lic. Josue Romero Alvarez",
    'website': "http://www.caribbeanflighttours.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Ventas',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale','contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/jcliente.xml',
        'views/jempleado.xml',
        'views/jfactura.xml',
        'views/jproducto.xml',
        'views/jventa.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}