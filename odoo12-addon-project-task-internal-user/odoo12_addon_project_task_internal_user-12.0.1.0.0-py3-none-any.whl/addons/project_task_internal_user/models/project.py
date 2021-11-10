from odoo import SUPERUSER_ID, api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    user_id = fields.Many2one(domain=[('share','=',False)])
    
