# -*- coding: utf-8 -*-
# from odoo import http


# class ../odoo-custom-addons/odoo15-addons/carlplane(http.Controller):
#     @http.route('/../odoo-custom-addons/odoo15-addons/carlplane/../odoo-custom-addons/odoo15-addons/carlplane', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../odoo-custom-addons/odoo15-addons/carlplane/../odoo-custom-addons/odoo15-addons/carlplane/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('../odoo-custom-addons/odoo15-addons/carlplane.listing', {
#             'root': '/../odoo-custom-addons/odoo15-addons/carlplane/../odoo-custom-addons/odoo15-addons/carlplane',
#             'objects': http.request.env['../odoo-custom-addons/odoo15-addons/carlplane.../odoo-custom-addons/odoo15-addons/carlplane'].search([]),
#         })

#     @http.route('/../odoo-custom-addons/odoo15-addons/carlplane/../odoo-custom-addons/odoo15-addons/carlplane/objects/<model("../odoo-custom-addons/odoo15-addons/carlplane.../odoo-custom-addons/odoo15-addons/carlplane"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../odoo-custom-addons/odoo15-addons/carlplane.object', {
#             'object': obj
#         })
