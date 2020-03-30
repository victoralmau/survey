# -*- coding: utf-8 -*-
# � 2013 Yannick Vaucher (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import _, api, exceptions, fields, models
from openerp.http import request
from dateutil.relativedelta import relativedelta
from datetime import datetime

import pytz

import logging
_logger = logging.getLogger(__name__)

class SurveyUserinput(models.Model):
    _inherit = 'survey.user_input'
    
    oniad_campaign_id = fields.Many2one(
        comodel_name='oniad.campaign',        
        string='Oniad Campaign'
    )
    oniad_user_id = fields.Many2one(
        comodel_name='oniad.user',        
        string='Oniad User'
    )    