# -*- coding: utf-8 -*-
{
    'name': "MT Easy Exchange Rate",

    'summary': "Easy to put exchange rate for currency",
    'description': """
        - Base currency rate auto convert by putting excel "=" formula.
        - It will convert automatically to actual rate.
        - No need to calculate at outside and copy and paste into rate.
        - It will auto calculate if you put formula.
    """,
    'author': "MYAT THU",
    'maintainer': 'Odoo Myanmar',
    'support': 'odoo.myatthu@gmail.com',
    'version': '12.0.0.1.0',
    'depends': ['base',],
    'data': [
        "views/views.xml",
    ],
    'images': ['static/description/icon.png'],

}
