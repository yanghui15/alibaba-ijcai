import scrapy
from scrapy.selector import Selector
from scra_test.items import ScraTestItem

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['tianqihoubao.com']
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    years = [2014,2015,2016]
    dates = []

    for y in years:
        for month in range(1,13):
            mx_days = days[month-1]
            if(month == 2 and y == 2016):
                mx_days = 29
            for day in range(1 , mx_days + 1):
                str_month = str(month)
                if(month < 10):
                    str_month = '0'+str(month)
                str_day = str(day)
                if(day < 10):
                    str_day = '0' + str(day)
                dates.append(str(y)+''+str_month+''+str_day)

    print dates

    f = open('locality.txt', 'r')
    line = f.readline()
    print line.split(',')
    localities = line.split(',')
    localities.remove('alashanmeng')

    start_urls = []

    for loc in localities:
        for date in dates:
            start_urls.append('http://www.tianqihoubao.com/lishi/'+loc+'/'+date+'.html')

    def parse(self, response):
        selector = Selector(response)
        print response.url
        urls = response.url.split('/')
        content = selector.xpath("//table//td/node()").extract()
        result = []
        for current in content:
            result.append(current.replace("\r\n","").replace(" ",""))
        print len(result)
        item = ScraTestItem()
        item['day_weather'] = result[5]
        item['day_wind'] = result[15]
        item['day_temperature'] = result[12].split('<b>')[1].split('</b>')[0]
        item['night_weather'] = result[9]
        item['night_wind'] = result[16]
        item['night_temperature'] = result[13].split('<b>')[1].split('</b>')[0]
        item['item_id'] = urls[4]+'_'+urls[5].split('.')[0]
        item['url'] = response.url
        print urls[4]+'_'+urls[5].split('.')[0]
        return item