# -*- coding: utf-8 -*-
# from odoo import http


# class FootstepsTools(http.Controller):
#     @http.route('/footsteps_tools/footsteps_tools/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/footsteps_tools/footsteps_tools/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('footsteps_tools.listing', {
#             'root': '/footsteps_tools/footsteps_tools',
#             'objects': http.request.env['footsteps_tools.footsteps_tools'].search([]),
#         })

#     @http.route('/footsteps_tools/footsteps_tools/objects/<model("footsteps_tools.footsteps_tools"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('footsteps_tools.object', {
#             'object': obj
#         })
