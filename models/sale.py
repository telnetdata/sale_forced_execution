# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, api

class SaleForcedExection(models.Model):
    """
    Add a new method for force execution
    """
    _inherit = ['sale.order']
    
    @api.multi
    def action_force_execution(self):
        for order in self:
            for line in order.order_line:
                line.qty_delivered = line.product_uom_qty

    @api.multi
    def action_force_no_invoice(self):
        for order in self:
            for line in order.order_line:
                if line.invoice_status in ('to invoice', ):
                    line.invoice_status = "no"
