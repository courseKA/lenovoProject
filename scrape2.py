class JarspiderSpider(scrapy.Spider):
    name = "jarspider"
    allowed_domains = ["jarcomputers.com"]
    start_urls = ["https://jarcomputers.com/Laptopi_cat_2.html?ref=c_1"]

    def parse(self, response):
        products = response.css('a.plttl::text').getall()
        
        for product in products:
            yield{
                'name': response.css('a.plttl::text').get(),
            }

        for i in range(2, 6):
            next_url = f"https://www.jarcomputers.com/laptopi-cat-2.html?ref=c_1&page={i}"
            yield response.follow(next_url, callback=self.parse)


