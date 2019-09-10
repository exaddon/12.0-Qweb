# -*- encoding: utf-8 -*-
{
    'name': 'Website Theme',
    'category':    'Theme/Services',
    'sequence': 7,
    'summary': 'A simple Theme example ',
    'version': '1.0',
    'description': "",
    'depends': [
        'website','theme_common',
    ],
    'images': [
        'static/description/website_theme_screenshot.jpg',
    ],
    'installable': True,
    'data': [

    #data
    'data/pictures.xml',

    #assets
    'views/assets.xml',

    #layout

    #pages
    ],
    'application': True,
}
