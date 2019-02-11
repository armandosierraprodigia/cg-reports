# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/cd-reports(http.Controller):
#     @http.route('/extra-addons/cd-reports/extra-addons/cd-reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/cd-reports/extra-addons/cd-reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/cd-reports.listing', {
#             'root': '/extra-addons/cd-reports/extra-addons/cd-reports',
#             'objects': http.request.env['extra-addons/cd-reports.extra-addons/cd-reports'].search([]),
#         })

#     @http.route('/extra-addons/cd-reports/extra-addons/cd-reports/objects/<model("extra-addons/cd-reports.extra-addons/cd-reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/cd-reports.object', {
#             'object': obj
#         })