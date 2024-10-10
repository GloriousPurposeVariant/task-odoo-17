from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    partner_type = fields.Selection(string='Type', selection=[("is_supplier", "Supplier"), ("is_customer", "Customer")])
    partner_domain = fields.Char(string='Partner Domain', compute='_compute_partner_domain')

    @api.depends('partner_type', 'company_id')
    def _compute_partner_domain(self):
        """
        Computes the domain for the partner_id field based on partner_type.

        If partner_type is 'is_supplier', the domain includes suppliers;
        if 'is_customer', it includes customers. The base domain allows for
        non-child partners or companies.
        """
        for record in self:
            base_domain = " '|', ('parent_id', '=', False), ('is_company', '=', True)"
            if record.partner_type == 'is_supplier':
                required_domain = "('is_supplier', '=', True)"
            elif record.partner_type == 'is_customer':
                required_domain = "('is_customer', '=', True)"
            else:
                required_domain = ""

            record.partner_domain = f"[{base_domain}, {required_domain}]"