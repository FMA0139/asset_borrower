#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class borrower_asset(models.Model):

    _name = "nc.borrower_asset"
    _description = "nc.borrower_asset"
    name = fields.Char( required=True, string="Name",  help="")
    description = fields.Text( string="Description",  help="")


    transaction_ids = fields.One2many(comodel_name="nc.transaction",  inverse_name="borrower_id",  string="Transactions",  help="")
