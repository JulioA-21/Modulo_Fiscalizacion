from odoo import models, fields

class ResPartner(models.Model):
     _inherit = "hr.employee"
     
     name = fields.Char(string="Name")