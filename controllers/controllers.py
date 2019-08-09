# -*- coding: utf-8 -*-
from odoo import http

# class PsTravelUmroh(http.Controller):
#     @http.route('/ps_travel_umroh/ps_travel_umroh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ps_travel_umroh/ps_travel_umroh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ps_travel_umroh.listing', {
#             'root': '/ps_travel_umroh/ps_travel_umroh',
#             'objects': http.request.env['ps_travel_umroh.ps_travel_umroh'].search([]),
#         })

#     @http.route('/ps_travel_umroh/ps_travel_umroh/objects/<model("ps_travel_umroh.ps_travel_umroh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ps_travel_umroh.object', {
#             'object': obj
#         })