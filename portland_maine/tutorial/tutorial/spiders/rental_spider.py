import scrapy


class rentalSpider(scrapy.Spider):
    name = "rental"

    start_urls = [
        'file:///Users/mac/data_visualization_web/portland_maine/tutorial/tutorial/spiders/southportland.html',
    ]

    def parse(self, response):
        num = 0
        for apts in response.css('div.styles__ListingCardContentContainer-y78yl0-6.ekushV'):

            yield{
                'name': apts.css('h3.styles__ListingCardName-y78yl0-8.cGrTjS::text').get(),
                'type': apts.css('div.styles__ListingCardBedDisplay-y78yl0-7.iPqMa::text').get(),
                'location': apts.css('div.styles__ListingCardText-y78yl0-9.hhRxyK::text').get(),
                'price': apts.css('div.styles__ListingCardPrice-y78yl0-17.cguwHc::text').get(),
                'link': 'https://rentalsapi.zillowgroup.com'+apts.css('a').attrib['href'],
            }
