import scrapy
from scrapy.http import HtmlResponse
from kino_parser.items import KinoParserItem
from scrapy.loader import ItemLoader


class KinometroSpider(scrapy.Spider):
    name = 'kinometro'
    allowed_domains = ['kinometro.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(len(kwargs.get("search"))):
            self.start_urls.append(
                f'https://www.kinometro.ru/release/show/month/{kwargs.get("search")[i][0]}/year/{kwargs.get("search")[i][1]}')
        print()


    def parse(self, response: HtmlResponse):
        links = response.xpath(
            "//td[@class='text-center']/../td/a[contains(@href, '/release/')]/@href").getall()
        print()
        for link in links:
            yield response.follow(link, callback=self.parse_movies)

    def parse_movies(self, response: HtmlResponse): #вводим loader, собираем item
        loader = ItemLoader(item=KinoParserItem(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('release_in_russia', "//div[@class='realiz-cont-t2']/text()")
        loader.add_xpath('cover', "//div[@class='realiz-img']/img/@src")
        loader.add_xpath('specifications', "//div[@class='realiz-cont']/div[@class='realiz-line']/span/text() | //div[@class='realiz-cont']/div[@class='realiz-line']/span/a/text()")
        loader.add_value('url', response.url)
        yield loader.load_item()

'''
Код парсера, написанный без ввода loader
'''
    # def parse_movies(self, response: HtmlResponse):
    #     print()
    #     name = response.xpath('//h1/text()').get()
    #     url = response.url
    #     release_in_russia = response.xpath("//div[@class='realiz-cont-t2']/text()").get()
    #     cover = response.xpath("//div[@class='realiz-img']/img/@src").get()
    #     specifications = response.xpath("//div[@class='realiz-cont']/div[@class='realiz-line']/span/text() | //div[@class='realiz-cont']/div[@class='realiz-line']/span/a/text()").getall()
    #     yield KinoParserItem(name=name, url=url, release_in_russia=release_in_russia, cover=cover, specifications=specifications)