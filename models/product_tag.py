

from odoo import api, fields, models

class PT(models.Model):
    _inherit = 'product.tag'
    code = fields.Char()
    def _compute_display_name(self):
        super()._compute_display_name()
        for pt in self:
            if pt.code:
                pt.display_name = "[%s] %s"% (pt.code, pt.display_name)
