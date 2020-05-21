import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class SpiderSpider(CrawlSpider):
    name = 'spider'
    allowed_domains = ['www.manhard.eu']
    start_urls = [
        'http://www.manhard.eu/webshop.asp?pa_id=59&level=2&product=002&pagename=messen.html']

    base_url = 'http://www.manhard.eu/webshop.asp'
    base_url1 = 'http://www.manhard.eu/'
    #headers= {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

    rules = (
        Rule(LinkExtractor(
            allow=r'.*&product=002.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//td/h1[1]/text()').extract_first()
        
        
        items = response.xpath('//a[@class="wit" and 1]/text()')
        for item in items:
            item1 = item.extract()
            images = response.xpath('//td[1]/img[1]/@src')
            for image in images:
                image1 = self.base_url1 + image.extract()
                links = response.xpath('//a[@class="wit" and 1]/@href')
                for link in links:
                    link1 = self.base_url + link.extract()
                    
                
                yield {
                    'Title': title,
                    'Item' : item1,
                    'Image': image1,
                    'Link' : link1,
                }

                    
        
        
        
        

        
