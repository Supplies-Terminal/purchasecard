# -*- coding: utf-8 -*-
from odoo import http
import json

class Purchasecard(http.Controller):
    @http.route('/purchasecard/purchasecard', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/purchasecard/purchasecard/print/<uuid>', auth='public')
    def list(self, uuid, **kw):
        purchasecard = http.request.env['st.purchasecard'].search([('uuid', '=', uuid)], limit=1)
        if not purchasecard:
            raise GraphQLError(_('Purchase Card does not exist.'))
        
        purchaseCardGrid = json.loads(purchasecard['data'])  
        
        return http.request.render('purchasecard.print', {
            'uuid': uuid,
            'data': purchasecard['data']
        })
