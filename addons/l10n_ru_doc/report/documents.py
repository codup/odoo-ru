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

import time
from openerp.report import report_sxw

class webkit_default(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(webkit_default, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'cr':cr,
            'uid': uid,
        })

report_sxw.report_sxw('report.sale.order.webkit',
                      'sale.order',
                      'l10n_ru_doc/report/order.htm',
                      parser=webkit_default)

report_sxw.report_sxw('report.account.invoice.webkit',
                      'account.invoice',
                      'l10n_ru_doc/report/invoice.htm',
                      parser=webkit_default)

report_sxw.report_sxw('report.account.invoice.bill.webkit',
                      'account.invoice',
                      'l10n_ru_doc/report/bill.htm',
                      parser=webkit_default)

report_sxw.report_sxw('report.account.invoice.act.webkit',
                      'account.invoice',
                      'l10n_ru_doc/report/act.htm',
                      parser=webkit_default)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: