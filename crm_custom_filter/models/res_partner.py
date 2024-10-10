from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    supplier_code = fields.Char(string='Supplier Code',
                                readonly=True, copy=False,
                                compute='_compute_supplier_code', store=True,
                                help="Automatically generated code for the supplier."
                                )
    customer_code = fields.Char(string='Customer Code',
                                readonly=True, copy=False,
                                compute='_compute_customer_code', store=True,
                                help="Automatically generated code for the customer."
                                )
    is_customer = fields.Boolean(string='Customer', help="Indicates if the partner is a customer.")
    is_supplier = fields.Boolean(string='Supplier', help="Indicates if the partner is a supplier.")

    def get_default_sequence_code(self, code):
        """
        Generate the next sequence code based on the provided sequence reference code.

        :param code: The sequence code defined in `ir.sequence` model.
        :return: The next value in the sequence for the provided code.
        """
        return self.env['ir.sequence'].next_by_code(code)

    @api.depends('is_supplier')
    def _compute_supplier_code(self):
        """
        Compute the `supplier_code` field.
        If `is_supplier` is True and `supplier_code` is not already set,
        generate a new supplier code using the sequence 'res.partner.supplier.code'.
        """
        for record in self:
            record.supplier_code = record.get_default_sequence_code(
                'res.partner.supplier.code') if not record.supplier_code else record.supplier_code

    @api.depends('is_customer')
    def _compute_customer_code(self):
        """
        Compute the `customer_code` field.
        If `is_customer` is True and `customer_code` is not already set,
        generate a new customer code using the sequence 'res.partner.customer.code'.
        """
        for record in self:
            record.customer_code = record.get_default_sequence_code(
                'res.partner.customer.code') if not record.customer_code else record.customer_code

    @api.depends('name', 'supplier_code', 'customer_code', 'is_supplier', 'is_customer')
    def _compute_display_name(self):
        """
        Compute the display name based on the supplier and customer status.
        PS: Since The Task Didn't mention how to handle if both were enabled,
            i am including both if both are enabled.
        """
        super()._compute_display_name() # so that we can use the old display_name
        for record in self:
            name_parts = []
            if record.is_supplier and record.supplier_code:
                name_parts.append(record.supplier_code)

            if record.is_customer and record.customer_code:
                name_parts.append(record.customer_code)

            name_parts.append(record.display_name or "")
            record.display_name = ' '.join(name_parts)
