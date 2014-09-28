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

{
    'name': 'Russia - Documents',
    'version': '1.2',
    'description': """
The module for print documents in accordance laws of Russia.
============================================================
Возможности:
    * Товарная накладная (ТОРГ-12)
    * Счет на оплату
    * Счет-фактура
    * Акт выполненных работ
    * Вывод подписей и печати
    """,
    'author': 'CodUP',
    'website': 'http://codup.com',
    'category': 'Localization',
    'sequence': 0,
    'depends': ['report_webkit_zoom','sale'],
    'demo': ['l10n_ru_doc_demo.xml'],
    'data': [
        'res_partner_view.xml',
        'res_company_view.xml',
        'res_users_view.xml',
        'res_bank_view.xml',
        'l10n_ru_doc_report.xml',
        'l10n_ru_doc_data.xml',
    ],
    'css': ['static/src/css/l10n_ru_doc.css'],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: