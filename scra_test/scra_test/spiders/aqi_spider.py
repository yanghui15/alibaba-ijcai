import scrapy
from scrapy.selector import Selector
from scra_test.items_aqi import ScraAqiItem

class WeatherSpider(scrapy.Spider):
    name = 'aqi'
    allowed_domains = ['tianqihoubao.com']
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    years = [2014,2015,2016]
    dates = []

    for y in years:
        for month in range(1,13):
            str_month = str(month)
            if(month < 10):
                str_month = '0'+str(month)
            dates.append(str(y)+''+str_month)

    print dates

    f = open('locality-2.txt', 'r')
    lines = f.readlines()
    localities = []
    for line in lines:
        localities.append(line.split(',')[1].replace("\n",""))
    print localities

    start_urls = []

    for loc in localities:
        for date in dates:
            start_urls.append('http://www.tianqihoubao.com/aqi/'+loc+'-'+date+'.html')

    def parse(self, response):
        selector = Selector(response)
        print response.url
        urls = response.url.split('/')
        content = selector.xpath("//table//tr").extract()
        length = len(content)
        result = []
        for idx in range(2 , length + 1):
            current = selector.xpath("//table//tr[%d]//td//text()"%idx).extract()
            result_item = []
            for current_item in current:
                result_item.append(current_item.replace("\r\n","").replace(" ",""))
            result.append(result_item)
        print len(result)
        items = []
        for result_item in result:
            item = ScraAqiItem()
            item['weather_quality'] = result_item[1]
            item['weather_aqi'] = result_item[2]
            item['weather_pm25'] = result_item[4]
            item['weather_pm10'] = result_item[5]
            item['weather_No2'] = result_item[6]
            item['weather_So3'] = result_item[7]
            item['weather_Co'] = result_item[8]
            item['weather_O3'] = result_item[9]
            item['item_id'] = urls[4].split('-')[0] + '_' + result_item[0]
            item['url'] = response.url
            items.append(item)
        print len(items)
        return items
