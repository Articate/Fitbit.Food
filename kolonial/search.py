import contextlib
import requests
import common.util as util
from kolonial.product import Product

from kolonial import const

class Search:
    search_url = const.BASE_URL + const.SEARCH_URL
    products = []

    def __init__(self):
        pass
    
    def query(self, query):
        url = self.search_url + query
        content = util.get_json(url)
        self.products = [Product(item)
                        for item in content['results'] 
                        if item['type'] == 'product']
        for p in self.products:
            print('{0} ({1}) - {2}, {3}. Id: {4}, url: {5}'.format(
                p.name, p.name_extra, p.price,
                p.unit_price, p.p_id, p.relative_url))
    
    def find_info(self, p_id):
        product = self.get_product(p_id)
        url = const.BASE_URL + product.relative_url
        print(url)
        content = util.get_raw(url)
        print(content)

    def get_product(self, p_id):
        for p in self.products:
            if p.p_id == p_id:
                return p