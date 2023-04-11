from odoo import fields, models


class ResCity(models.Model):
    _name = 'res.country.state.city'
    _description = "State City"
    
    name = fields.Char("City", required=True)
    state_id = fields.Many2one('res.country.state', "State")
    
    
class ResCountryState(models.Model):
    _inherit = 'res.country.state'
    
    city_ids = fields.One2many('res.country.state.city', 'state_id', "City")