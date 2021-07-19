from odoo import models, fields

class ResPartner(models.Model):
     _inherit = "hr.employee"
     
     name = fields.Char(string="Name")
     user_id = fields.Many2one('res.users','Current User')