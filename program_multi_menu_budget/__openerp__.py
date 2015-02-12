# -*- coding: utf-8 -*-

##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Savoir-faire Linux (<www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Program Budget - Multi-Menu Bindings',
    'version': '1.1',
    'category': 'Program',
    'summary': 'Account Budget bindings to Results',
    'description': '''
Program Budget - Multi-Menu Bindings
====================================

Separate Roles and Regions by menu

Contributors
------------

* Sandy Carter (sandy.carter@savoirfairelinux.com)
''',
    'author': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'depends': [
        'program_budget',
        'program_multi_menu',
    ],
    'data': [
        'ir_actions_act_window_data.xml',
        'program_result_view.xml',
        'program_result_country_view.xml',
    ],
    'auto_install': True,
    'installable': True,
}