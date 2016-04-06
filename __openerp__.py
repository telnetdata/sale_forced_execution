# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale forced execution',
    
    'version' : '1.0',
    
    'summary': 'Add force execution action to sale orders',
    
    'sequence': 28,
    
    'description': """
Sale Forced Execution
====================

Add a new action to sale orders, that set delivered quantities to ordered quantities. 
    """,
    
    'author': "Telnet Data",
    
    'website': "http://www.telnetservizi.it",
    
    'category': 'Sales Management',
    
    'depends' : ['sale', 'stock'],
    
    'data': [
        'views/sale_view.xml',
    ],
    
    'installable': True,
    'application': False,
    'auto_install': False,
}
