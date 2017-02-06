import scrapy
from scrapy.selector import Selector

class Locality_Spider(scrapy.Spider):
    name = 'locality'
    allowed_domains = ['tianqihoubao.com']
    start_urls = ['http://www.tianqihoubao.com/lishi/']

    def parse(self, response):
        selector = Selector(response)
        print response.url
        urls = response.url.split('/')
        content = selector.xpath("//a").extract()
        result = []
        for current in content:
            if(('html' in current) and ('/lishi/' in current) and ('.' in current)):
                print current
                result.append(current.split('"')[1].split('/lishi/')[1].split('.')[0])
        self.save_to_file(result)

    def save_to_file(self , result):
        f = open('locality.txt', 'w')
        for current in result:
            f.write(current+',')
        f.close()