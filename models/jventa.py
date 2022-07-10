# -*- coding: utf-8 -*-

from odoo import models, fields

class JVenta(models.Model):
    _inherit = 'sale.order'
    
    name = fields.Char(default=lambda self: 'Nueva Reserva de Pasaje')
    vuelo_img = fields.Image()
    date_born = fields.Date(string="Fecha de Nacimiento")
    passport = fields.Char(string="Numero de Pasaporte",required=True)
    passport_down = fields.Date(string="Fecha de Expiracion del Pasaporte",required=True)
    vuelo_origen = fields.Char(string="Origen del Vuelo",required=True)
    vuelo_dest = fields.Char(string="Destino del Vuelo",required=True)
    date_ida = fields.Date(string="Fecha de Ida",required=True)
    date_regreso = fields.Date(string="Fecha de Regreso",required=True)
    vacunado = fields.Boolean(string="Vacunado")
    pcr = fields.Boolean(string="PCR")
    pcr_archivo = fields.Binary(string="Resultado del PCR")