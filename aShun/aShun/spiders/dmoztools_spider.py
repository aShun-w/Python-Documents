import scrapy
from aShun.items import AshunItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = ['http://www.dmoztools.net/News/']

    def parse(self,response):
##        filename = response.url.split("/")[-2]
##        with open(filename,'wb') as f:
##            f.write(response.body)
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath("//section/div/div/div/div[@class='title-and-desc']")

        items = []
        
        for site in sites:
            item = AshunItem()
            item['title'] = site.xpath("a/div/text()").extract()
            item['link'] = site.xpath("a[@target='_blank']/@href").extract()
            item['desc'] = site.xpath("div/text()").extract()
##            print("title=%s , link=%s , desc=%s " % (title,link,desc))
            items.append(item)
        return items
            
    
