-*- coding: utf-8 -*-
from odoo import http


class Purchasecard(http.Controller):
    @http.route('/purchasecard/purchasecard', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/purchasecard/purchasecard/print/<uuid>', auth='public')
    def list(self, **kw):
        return http.request.render('purchasecard.print', {
            'uuid': uuid,
        })
