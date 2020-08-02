import scrapy
from ..items import AmazonBestsellersItem

class BestsellerSpider(scrapy.Spider):
    name = 'bestseller'
    page_number = 2
    allowed_domains = ['https://www.amazon.com/Best-Sellers/zgbs']
    start_urls = ['https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_1?_encoding=UTF8&pg=1']

    def parse(self, response):
        item = AmazonBestsellersItem()
        items = response.css ('li.zg-item-immersion')
        for i in items:
            item_name = i.css('div::text').extract()
            price = i.css('.p13n-sc-price::text').extract()
            image = i.css('img::attr(src)').extract()
            rank1 = i.css('.zg-badge-text::text').extract()

            item['item_name'] = item_name
            item['price'] = price
            item['image'] = image
            item['rank1'] = rank1
            yield item

        next_page = 'https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_1?_encoding=UTF8&pg=' + str(BestsellerSpider.page_number)
        if BestsellerSpider.page_number < 3:
            yield response.follow(next_page, callback = self.parse, dont_filter=True)
            BestsellerSpider.page_number += 1

