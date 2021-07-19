import re
from odoo import models, fields,api

class AtmInspection(models.Model):
    _name = "atm.inspection"

    name = fields.Char(string='Inspection Number',size=30, required=True, copy=False, index=True, readonly=True,default=lambda self: ('New'))
    cedule = fields.Char(string="cedule",size=8)
        # Dates
    date_start = fields.Date(string="Start Date",required=True)
    date_start_charge = fields.Date(string="Start charged  date")
    date_end_charge = fields.Date(string="End charge date")
    date_start_view = fields.Date(string="Start View date")
    date_end_view = fields.Date(string="End View date")
    date_start_intimation = fields.Date(string="Start Intimation date")
    date_end_intimation = fields.Date(string="End Intimation date")
    date_start_determinative = fields.Date(string="Start determinative date")
    date_end_determinative = fields.Date(string="End determinative date")

        # Amounts
    debt_iibb  = fields.Float(string="IIBB Debt")
    debt_agent  = fields.Float(string="Agent Debt")
    debt_ipa  = fields.Float(string="IPA Debt")
    debt_sell  = fields.Float(string="Sell Debt")
    debt_property  = fields.Float(string="Property Debit")
    amount_interest  = fields.Float(string="Amount Interest")
    amount_fine  = fields.Float(string="Amount Fine")
    debt_total  = fields.Float(compute="_debt_total",string="Debt Total",onlyread=True)
    positive_balance  = fields.Float(string="Positive Balance")
    interest_fine  = fields.Float(compute="_interest_fine", string="Interest Fine")
    total_capital  = fields.Float(compute="_total_capital", string="Total Capital")
        # Relations
    current_user = fields.Many2one('res.users','Current User', default=lambda self: self.env.user)
    expedient_id = fields.Many2one('atm.expedient',string='Expedient',required=True)
    agent_id = fields.Many2one('hr.employee',string='Agent',required=True)
    client_id = fields.Many2one('res.partner',string='Client',required=True)
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

    def _debt_total(self):
        for rec in self:
            rec.debt_total = 0
            rec.debt_total = rec.debt_total + rec.debt_iibb + rec.debt_agent + rec.debt_sell + rec.debt_property + rec.amount_interest + rec.amount_fine + rec.debt_ipa
    def _total_capital(self):
        for rec in self:
            rec.total_capital = 0
            rec.total_capital = rec.total_capital + rec.debt_iibb + rec.debt_agent + rec.debt_sell + rec.debt_property + rec.debt_ipa
           
    def _interest_fine(self):
            for rec in self:
                rec.interest_fine = 0
                rec.interest_fine = rec.interest_fine + rec.amount_interest + rec.amount_fine