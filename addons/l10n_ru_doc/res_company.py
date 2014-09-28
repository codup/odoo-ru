# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 CodUP (<http://codup.com>).
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

from openerp.osv import fields, osv

class res_company(osv.osv):
    _name = 'res.company'
    _inherit = 'res.company'

    _columns = {
        'inn': fields.related('partner_id', 'inn', string="INN", type="char", size=12),
        'kpp': fields.related('partner_id', 'kpp', string="KPP", type="char", size=9),
        'okpo': fields.related('partner_id', 'okpo', string="OKPO", type="char", size=14),
        'chief_id': fields.many2one('res.users', 'Chief'),
        'accountant_id': fields.many2one('res.users', 'General Accountant'),
        'print_facsimile': fields.boolean('Print Facsimile', help="Check this for adding Facsimiles of responsible persons to documents."),
        'print_stamp': fields.boolean('Print Stamp', help="Check this for adding Stamp of company to documents."),
        'stamp': fields.binary("Stamp"),
        'print_anywhere': fields.boolean('Print Anywhere', help="Uncheck this, if you want add Facsimile and Stamp only in email."),
    }

    _defaults = {
        'print_anywhere': True,
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: