from odoo import models, fields,api

class AtmInspection(models.Model):
    _name = "atm.inspection"

    name = fields.Char(string='Inspection Number',size=30, required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    cedule = fields.Char(string="cedule",size=8)
    date_start = fields.Date(string="Start Date")
    date_end_charge = fields.Date(string="End charge date")
    date_end_view = fields.Date(string="End View date")
    date_end_intimation = fields.Date(string="End Intimation date")
    date_end_determinative = fields.Date(string="End determinative date")
    debt_iibb  = fields.Float(string="IIBB Debt")
    debt_agent  = fields.Float(string="Agent Debt")
    debt_ipa  = fields.Float(string="IPA Debt")
    debt_sell  = fields.Float(string="Sell Debt")
    debt_property  = fields.Float(string="Property Debit")
    amount_interest  = fields.Float(string="Amount Interest")
    amount_fine  = fields.Float(string="Amount Fine")
    debt_total  = fields.Float(string="Debt Total")
    expedient_id = fields.Many2one('atm.expedient',string='Expedient')
    agent_id = fields.Many2one('hr.employee',string='Agent')
    client_id = fields.Many2one('res.partner',string='Client')
    state  = fields.Selection([('draft', 'Draft'),('charge_actuation', 'Charge Actuation'),('documentation_solicited', 'Documentation Solicited'),\
    ('documentation_solicited_overdue', 'Documentation Solicited Overdue'),('presunte_debt', 'Presunte Debt'),('view', 'View'),('intimation', 'Intimation')\
    ,('determinative', 'Determinative'),('legal', 'Legal'),('played', 'Played')], default="draft")

    def action_btn_draft(self):
        self.state = 'draft'
    def action_btn_charge_actuation(self):
        self.state = 'charge_actuation'
    def action_btn_documentation_solicited(self):
        self.state = 'documentation_solicited'
    def action_btn_documentation_solicited_overdue(self):
        self.state = 'documentation_solicited_overdue'    
    def action_btn_presunte_debt(self):
        self.state = 'presunte_debt'
    def action_btn_view(self):
        self.state = 'view'
    def action_btn_intimation(self):
        self.state = 'intimation'
    def action_btn_determinative(self):
        self.state = 'determinative'
    def action_btn_legal(self):
        self.state = 'legal'
    def action_btn_played(self):
        self.state = 'played'

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('atm.inspection')
        result = super(AtmInspection, self).create(vals)
        return result
