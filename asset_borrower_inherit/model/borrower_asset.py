#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class borrower_asset(models.Model):
    _name = "nc.borrower_asset"
    _inherit = "nc.borrower_asset"
