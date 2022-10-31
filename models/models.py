# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class footsteps_tools(models.Model):
#     _name = 'footsteps_tools.footsteps_tools'
#     _description = 'footsteps_tools.footsteps_tools'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
