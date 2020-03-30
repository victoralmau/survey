# -*- coding: utf-8 -*-
{
    'name': 'Ont Survey Web',
    'version': '10.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'web', 'ont_base_survey'],
    'data': [
        'views/template.xml',
    ],
    'qweb': ['static/src/xml/buttons.xml'],        
    'installable': True,
    'auto_install': False,    
}