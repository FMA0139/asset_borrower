#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class assets(models.Model):

    _name = "nc.assets"
    _description = "nc.assets"
    name = fields.Char( required=True, string="Name",  help="")
    amount = fields.Integer( string="Amount",  help="")


