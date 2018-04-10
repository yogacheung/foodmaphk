import scrapy
import json

class openrice_spider(scrapy.Spider):
    name = 'openrice_spider'

    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'
    }

    def start_requests(self):        
        with open("openrice_urls.txt", "rb") as f:
            self.start_urls = f.read().split("\n")

        for url in self.start_urls:           
            yield scrapy.Request(url=url, callback=self.parse)                

    def parse(self, response):
        data = json.loads(response.css('script[type="application/ld+json"]::text').extract_first())
        reviews = response.css('span[itemprop="reviewCount"]::text').extract_first()
        rating = response.css('div.score-div::text').extract()
        yield { 
                'name' : data['name'],
                'cuisine' :  data['servesCuisine'].split(","),
                'price-range' : data['priceRange'],
                'address' : [data['geo']['latitude'], data['geo']['longitude']],
                'rating' : rating, 
                'reviews' : reviews, 
                'district' : data['address']['addressLocality'],
                'url' : response.url
        }
