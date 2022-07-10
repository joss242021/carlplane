# -*- coding: utf-8 -*-

from odoo import models, fields

class JCliente(models.Model):
    _inherit = 'res.partner'
            
    number_id = fields.Char(string="C.i-Identificacion-Social:",required=True)
    date_born = fields.Date(string="Fecha de Nacimiento")
    status_civil = fields.Selection(
        string="Estado Civil",
        selection = [
            ('soltero',"Soltero"),
            ('casado',"Casado"),
            ('divorsiado',"Divorsiado"),
            ('otros',"Otros"),
            ]
        )    
    passport = fields.Char(string="Numero de Pasaporte",required=True)
    passport_up = fields.Date(string="Fecha de Emision del Pasaporte",required=True)
    passport_down = fields.Date(string="Fecha de Expiracion del Pasaporte",required=True)