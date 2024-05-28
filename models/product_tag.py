

from odoo import api, fields, models

class PT(models.Model):
    _inherit = 'product.tag'
    code = fields.Char()
