from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    partner_domain = fields.Char(string='Partner Domain', compute='_compute_partner_domain')


    @api.depends('move_type', 'company_id')
    def _compute_partner_domain(self):
        """
        Computes the domain for the partner_id field based on the move_type.

        If move_type is 'in_invoice', the domain includes suppliers;
        if 'out_invoice', it includes customers. The domain also filters
        by company_id, allowing for non-specific company partners.
        """
        for record in self:
            default_domain = f"('company_id', 'in', (False, {record.company_id.id}))"
            if record.move_type == 'in_invoice':
                record.partner_domain = f"[{default_domain}, ('is_supplier', '=', True)]"
            elif record.move_type == 'out_invoice':
                record.partner_domain = f"[{default_domain}, ('is_customer', '=', True)]"
            else:
                record.partner_domain = f"[{default_domain}]"
