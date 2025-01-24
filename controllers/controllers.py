# -*- coding: utf-8 -*-
# from odoo import http


# class Alvaroejercicio(http.Controller):
#     @http.route('/alvaroejercicio/alvaroejercicio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alvaroejercicio/alvaroejercicio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alvaroejercicio.listing', {
#             'root': '/alvaroejercicio/alvaroejercicio',
#             'objects': http.request.env['alvaroejercicio.alvaroejercicio'].search([]),
#         })

#     @http.route('/alvaroejercicio/alvaroejercicio/objects/<model("alvaroejercicio.alvaroejercicio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alvaroejercicio.object', {
#             'object': obj
#         })

