from odoo import models, fields,api

class AtmExpedient(models.Model):
    _name = "atm.expedient"

    name = fields.Char(string="Expedient Number",required=True)
    fiscalyear = fields.Char(string="Fiscal Year", size =4,required=True)
    date_start = fields.Date(string="Date star Expedient")
    description = fields.Text(string="Description")
    type  = fields.Selection([('administration', 'Administration'),('fiscalizaion_inspection', 'Fiscalization_Inspection')],required=True)
    location  = fields.Selection([('externa', 'Externa'),('fiscalization', 'Fiscalization'),('direccion', 'Direccion'),('liquidacion', 'Liquidacion'),('juridico', 'Juridico'),('otros', 'Otros')])
   