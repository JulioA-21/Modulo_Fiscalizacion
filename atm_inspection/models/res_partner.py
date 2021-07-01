from odoo import models, fields

class ResPartner(models.Model):
     _inherit = "res.partner"
     
     taxpayer = fields.Boolean(string="Tax Payer", default=False)