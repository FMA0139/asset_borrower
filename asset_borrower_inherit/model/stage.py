#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class stage(models.Model):
    _name = "nc.stage"
    _inherit = "nc.stage"
