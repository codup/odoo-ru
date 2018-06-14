# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2015-2018 CodUP (<http://codup.com>).
#
##############################################################################

from odoo import api, models
from odoo.addons.l10n_ru_doc.report_helper import QWebHelper

class RuBillReport(models.AbstractModel):
    _name = 'report.l10n_ru_doc.report_bill'

    @api.multi
    def get_report_values(self, docids, data=None):
        docs = self.env['account.invoice'].browse(docids)
        return {
            'helper': QWebHelper(),
            'doc_ids': docs.ids,
            'doc_model': 'account.invoice',
            'docs': docs
        }
