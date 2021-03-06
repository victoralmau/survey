# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Survey user input expired",
    "version": "12.0.1.0.0",
    "author": "Odoo Nodriza Tech (ONT), "
              "Odoo Community Association (OCA)",
    "website": "https://nodrizatech.com/",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "survey"
    ],
    "data": [
        "data/ir_cron.xml",
        "views/survey_user_input_view.xml",
    ],
    "installable": True
}
