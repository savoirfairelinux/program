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

from openerp.osv import fields, orm
from openerp.tools.translate import _


class program_action_level(orm.Model):

    _name = 'program.action.level'

    def create(self, cr, uid, data, context=None):
        if data.get('depth', -1) < 0:
            raise orm.except_orm(
                _('Error!'),
                _('Depth must be greater than or equal to 0.')
            )
        return super(program_action_level, self).create(
            cr, uid, data, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        if vals.get('depth', 0) < 0:
            raise orm.except_orm(
                _('Error!'),
                _('Depth must be greater than or equal to 0.')
            )
        return super(program_action_level, self).write(
            cr, uid, ids, vals, context=context)

    def name_get(self, cr, uid, ids, context=None):
        if not isinstance(ids, list):
            ids = [ids]
        return [(line.id, (line.code and line.code + ' - ' or '') + line.name)
                for line in self.browse(cr, uid, ids, context=context)]

    _columns = {
        'name': fields.char(
            'Name', size=128, required=True, select=True, translate=True),
        'action': fields.one2many(
            'program.action', 'action_level', string='Action'),
        'code': fields.char('Code', size=32),
        'depth': fields.integer('Level', required=True),
    }
    _defaults = {
        'depth': 1,
    }
