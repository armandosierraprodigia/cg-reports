# -*- coding: utf-8 -*-
{
    'name': "Reportes CG",

    'summary': """
        Modificaciones a los repotes de presupuestos, solicitud de presupuestos, facturas""",

    'description': """
        Modificación de los reportes agregando nuevas columnas y totales a los reportes
    """,

    'author': "Prodigia",
    'website': "http://www.prodigia.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [        # 'security/ir.model.access.csv',
        'views/report_invoice_inherit.xml',
        'views/report_purchasequotation_document.xml',
        'views/report_saleorder_document.xml',
        'views/report_purchaseorder_document_inherit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
