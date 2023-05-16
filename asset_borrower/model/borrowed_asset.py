#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class borrowed_asset(models.Model):

    _name = "nc.borrowed_asset"
    _description = "nc.borrowed_asset"
    name = fields.Char( required=True, string="Name",  help="")
    amount = fields.Char( string="Amount",  help="")


