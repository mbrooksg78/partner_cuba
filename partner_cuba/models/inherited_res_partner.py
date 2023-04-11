
from odoo import api, fields, models
from odoo.tools.translate import _


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    city_id = fields.Many2one('res.country.state.city', "City")
    
    @api.onchange('country_id')
    def onchange_country(self):
        print("ONCH: {} {}".format(self.country_id, self.env.ref('base.cu').id))
        cuba_id = self.env.ref('base.cu')
        if self.country_id == cuba_id:
            return {
                'domain': {
                    'state_id': [('country_id', '=', self.env.ref('base.cu'))]
                }
            }
            
    @api.onchange('state_id')
    def onchange_city(self):
        if self.country_id == self.env.ref('base.cu'):
            return {
                'domain': {
                    'city_id': [('state_id', '=', self.state_id.id)]
                }
            }
    