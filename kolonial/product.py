import common.util as util

class Product:
    def __init__(self, json):
        self.p_id = json['id']
        self.relative_url = json['url']
        
        html = util.parse_html(json['html'])
        divs = html.select('div')
        self.name = self.get_name(divs)
        self.name_extra = self.get_name_extra(divs)
        self.price = self.get_price(divs)
        self.unit_price = self.get_unit_price(divs)

    def get_name(self, divs):
        for div in divs:
            if 'name' in div['class']:
                return div.text
    
    def get_name_extra(self, divs):
        for div in divs:
            if 'name-extra' in div['class']:
                return div.text
        return None

    def get_price(self, divs):
        for div in divs:
            if 'price' in div['class']:
                return div.text
    
    def get_unit_price(self, divs):
        for div in divs:
            if 'unit-price' in div['class']:
                return div.text
        return None
