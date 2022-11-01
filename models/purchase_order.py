from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    delivery_status = fields.Selection([
        ('nothing', 'Nothing to Receive Yet'),
        ('pending', 'Pending Receipt'),
        ('received', 'Received'),
        ('cancel', 'Receipt Cancelled'),
    ], default='nothing', string="Delivery/Receipt Status", compute='get_delivery_status')

    @api.depends('state')
    def get_delivery_status(self):
        for rec in self:
            if rec.state == 'purchase':
                rec.delivery_status = 'nothing'
    #             if rec.picking_ids:
    #                 for items in rec.picking_ids:
    #                     if items.state != 'done':
    #                         rec.delivery_status = 'pending'
    #                     if items.state == 'cancel':
    #                         rec.delivery_status = 'cancel'
    #                     else:
    #                         rec.delivery_status = 'received'
    #         else:
    #             rec.delivery_status = 'nothing'


