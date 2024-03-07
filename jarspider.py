import scrapy

class JarspiderSpider(scrapy.Spider):
     name = "jarspider"
     allowed_domains = ["jarcomputers.com"]
     start_urls = ["https://jarcomputers.com/Laptopi_cat_2.html?ref=c_1"]
    
     def parse(self, response):
         for link in response.css('div#content.c2c.resp_600 div.breadcrumb a::attr(href)').getall()[1]:
             yield response.follow(link, callback=self.parse_laptop)

         for i in range(1,6):
             next_page = f'https://www.jarcomputers.com/laptopi-cat-2.html?ref=c_1&page={i}'
             yield response.follow(next_page, callback=self.parse)
             
     def parse_laptop(self, response):
             yield{
                 'name': response.css('a.plttl::text').re(r'Lenovo.*'),
                 'price' : response.css('div.row-price').get().replace('<div class="row-price">\n<div class="price\
 price-product">', '').replace('<span class="price2">', '').replace('<span>',\
 '').replace('</span></span></div>\n</div>', '')
             }
