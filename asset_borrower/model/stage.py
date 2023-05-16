#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class stage(models.Model):

    _name = "nc.stage"
    _description = "nc.stage"
    name = fields.Char( required=True, string="Name",  help="")
    descriptiom = fields.Text( string="Descriptiom",  help="")


    transaction_ids = fields.One2many(comodel_name="nc.transaction",  inverse_name="stage_id",  string="Transactions",  help="")
