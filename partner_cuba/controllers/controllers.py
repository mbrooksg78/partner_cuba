# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerCuba(http.Controller):
#     @http.route('/partner_cuba/partner_cuba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_cuba/partner_cuba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_cuba.listing', {
#             'root': '/partner_cuba/partner_cuba',
#             'objects': http.request.env['partner_cuba.partner_cuba'].search([]),
#         })

#     @http.route('/partner_cuba/partner_cuba/objects/<model("partner_cuba.partner_cuba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_cuba.object', {
#             'object': obj
#         })
