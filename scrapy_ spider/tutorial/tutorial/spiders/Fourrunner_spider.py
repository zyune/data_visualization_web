import scrapy


class FourrunnerSpider(scrapy.Spider):
    name = "Fourrunner"

    start_urls = [
        'https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=toyota&maximum_distance=all&mileage_max=&models[]=toyota-4runner&page_size=20&sort=best_match_desc&stock_type=used&year_max=2018&year_min=2018&zip=04103',
    ]

    def parse(self, response):
        for cars in response.css('div.vehicle-card'):

            yield{
                'name': cars.css('h2.title::text').get(),
                'price': cars.css('span.primary-price::text').get().replace('$', ''),
                'millage': cars.css('div.mileage::text').get().replace(' mi', ''),
                'link': 'https://www.cars.com'+cars.css('a.vehicle-card-link').attrib['href']
            }

        for a in response.css('a.sds-button.sds-button--secondary.sds-pagination__control'):
            if a.attrib['aria-label'] == 'Next page':
                next_page = 'https://www.cars.com' + \
                    a.attrib['href'].replace('amp;', '')

                # next_page = 'https://www.cars.com' + \
                #     response.css(
                #         'a.sds-button.sds-button--secondary.sds-pagination__control').attrib['href'].replace('amp;', '')
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
