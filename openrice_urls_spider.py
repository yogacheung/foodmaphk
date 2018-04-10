import scrapy

class openrice_urls_spider(scrapy.Spider):
    name = "openrice_urls_spider"

    start_urls = [        
        "https://www.openrice.com/en/hongkong/restaurants?where=shatin",
        "https://www.openrice.com/en/hongkong/restaurants/district/mong-kok",            
        "https://www.openrice.com/en/hongkong/restaurants/district/tsim-sha-tsui",
        "https://www.openrice.com/en/hongkong/restaurants/district/causeway-bay",    
    ]

    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'
    }

    def start_requests(self):
        for i in range(4):

            for j in range(1,18):
                if j == 1:
                    yield scrapy.Request(url=self.start_urls[i], callback=self.parse)            
                else:
                    if i == 0: 
                        url2 = self.start_urls[i] + "&page=" + str(j)
                        yield scrapy.Request(url=url2, callback=self.parse)            
                    else:
                        url2 = self.start_urls[i] + "?page=" + str(j)
                        yield scrapy.Request(url=url2, callback=self.parse)            

    def parse(self, response):                    
        res_url = response.css('h2[class=title-name] a::attr(href)').extract()
        for i in res_url:
            mod_res_url = "https://www.openrice.com" + i + "\n"            
            with open("openrice_urls.txt", "a") as f:
                f.write(mod_res_url)
