#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class uom(models.Model):

    _name = "nc.uom"
    _description = "nc.uom"
    name = fields.Char( required=True, string="Name",  help="")
    unit_of_measure = fields.Char( string="Unit of measure",  help="")
    type = fields.Selection(selection=[('smaller','Smaller'),('reference','Reference'),('bigger','Bigger')],  string="Type",  help="")
    ratio = fields.Integer( string="Ratio",  help="")
    active = fields.Selection(selection=[('yes','Yes'),('no','No')],  string="Active",  help="")


