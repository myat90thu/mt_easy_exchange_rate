# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class CurrencyRate(models.Model):
    _inherit = 'res.currency.rate'

    calc_rate = fields.Char(string = "Rate(Formula)", help = "You can use = for formula like excel calculation", default = '=')

    @api.multi
    @api.onchange('calc_rate')
    def calculate_rate(self):
        if self.calc_rate:
            if self.calc_rate.startswith("="):
                result = self.calc_rate.split("=")[1]
                self.rate = eval(result) if result else self.rate
            else:
                raise ValidationError(_("You must fill formula start with '='."))
