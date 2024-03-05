import scrapy

class JarspiderSpider(scrapy.Spider):
    name = "jarspider"
    allowed_domains = ["jarcomputers.com"]
    start_urls = ["https://jarcomputers.com/Laptopi_cat_2.html?ref=c_1"]

    def parse(self, response):
        products = response.css('div#products-container div ol#product_list.p1 li.sProduct.p.e-7 div.s2 ul.pprop \
li.list_brand.brand div.brand-name a.brand-name')\
.get().replace('<a href="', ' ').replace('" class="brand-name" style>Lenovo</a>', '')

        for i in range(2, 6):
            next_url = f"https://www.jarcomputers.com/laptopi-cat-2.html?ref=c_1&page={i}"
            yield response.follow(next_url, callback=self.parse)

    def parse_laptops(self, response):
            yield {
            'name': response.css('a.plttl::text').get(),
            'screensize': response.css('a.plttl::text').get().split()[11]
        }