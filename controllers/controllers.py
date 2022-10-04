# -*- coding: utf-8 -*-
from odoo import http
import json

class Purchasecard(http.Controller):
    @http.route('/purchasecard/purchasecard', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/purchasecard/purchasecard/print/<uuid>/<locale>', auth='public')
    def list(self, uuid, locale, **kw):
        purchasecard = http.request.env['st.purchasecard'].search([('uuid', '=', uuid)], limit=1)
        if not purchasecard:
            return http.request.render('purchasecard.print-error', {
                'message': uuid,
            })

        locale = get_nearest_lang(local)
        if not locale:
            locale = 'en_US'
            
        website = http.request.env['website'].browse(purchasecard['website_id'])

        lines = 20
        # 获取指定语言的商品名称
        purchaseCardGrid = json.loads(purchasecard['data'])
        data = {}
        for tableIndex in range(0, len(purchaseCardGrid)):
            total = len(purchaseCardGrid[tableIndex]['items'])
            for itemIndex in range(0, total):
                productInfo = http.request.env['product.product'].with_context(lange=locale).browse(purchaseCardGrid[tableIndex]['items'][itemIndex]['product_id'])
                if productInfo:
                    purchaseCardGrid[tableIndex]['items'][itemIndex]['name'] = productInfo['name']
            # 补全空行
            if total < lines:
                for other in range(total, lines):
                    purchaseCardGrid[tableIndex]['items'][other] = {
                        product_id: 0,
                        name: '&nbsp;',
                        unit: '&nbsp;'
                    }
        
        return http.request.render('purchasecard.print', {
            'uuid': uuid,
            'locale': locale,
            'title': website.name,
            'data': purchaseCardGrid
        })
        
    @classmethod
    def _get_frontend_langs(cls):
        return [code for code, _ in request.env['res.lang'].get_installed()]

    @classmethod
    def get_nearest_lang(cls, lang_code):
        """ Try to find a similar lang. Eg: fr_BE and fr_FR
            :param lang_code: the lang `code` (en_US)
        """
        if not lang_code:
            return False
        short_match = False
        short = lang_code.partition('_')[0]
        for code in cls._get_frontend_langs():
            if code == lang_code:
                return code
            if not short_match and code.startswith(short):
                short_match = code
        return short_match
