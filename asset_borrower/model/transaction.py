#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class transaction(models.Model):

    _name = "nc.transaction"
    _description = "nc.transaction"
    name = fields.Char( required=True, string="Name",  help="")
    transaction_date = fields.Date( string="Transaction date",  help="")
    borrow_time = fields.Date( string="Borrow time",  help="")
    return_time = fields.Date( string="Return time",  help="")
    purposes = fields.Char( string="Purposes",  help="")
    location = fields.Char( string="Location",  help="")
    description = fields.Text( string="Description",  help="")


    borrower_id = fields.Many2one(comodel_name="nc.borrower_asset",  string="Borrower",  help="")
    stage_id = fields.Many2one(comodel_name="nc.stage",  string="Stage",  help="")
    borrowed_ids = fields.Many2many(comodel_name="nc.assets",  string="Borroweds",  help="")
