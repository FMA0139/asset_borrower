#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class assets(models.Model):
    _name = "nc.assets"
    _inherit = "nc.assets"
