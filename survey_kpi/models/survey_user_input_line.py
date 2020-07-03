# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input_line'
    
    survey_kpi_id = fields.Many2one(
        comodel_name='survey.kpi',
        string='Survey Kpi'
    )                                                                        