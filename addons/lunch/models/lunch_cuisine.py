from odoo import api, fields, models

class LunchCuisine(models.Model):
    _name = 'lunch.cuisine'
    _description = 'Lunch Cuisine'
    _inherit = ['image.mixin']

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    supplier_ids = fields.Many2many('lunch.supplier', 'cuisine_id', string='Vendors')
