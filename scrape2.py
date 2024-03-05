class JarspiderSpider(scrapy.Spider):
    name = "jarspider"
    allowed_domains = ["jarcomputers.com"]
    start_urls = ["https://jarcomputers.com/Laptopi_cat_2.html?ref=c_1"]

    def parse(self, response):
        products = response.css('div#products-container div ol#product_list.p1 li.sProduct.p.e-7 div.s2 ul.pprop \
li.list_brand.brand div.brand-name a.brand-name')\
.get().replace('<a href="', ' ').replace('" class="brand-name" style>Lenovo</a>', '')
        for product in products:
            yield{
                'name': response.css('a.plttl::text').get(),
                'screensize': response.css('a.plttl::text').get().split()[11]
            }
