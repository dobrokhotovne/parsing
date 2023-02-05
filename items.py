import scrapy
from itemloaders.processors import MapCompose, TakeFirst


class KinoParserItem(scrapy.Item):

    _id = scrapy.Field(input_processor=MapCompose(int), output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    release_in_russia = scrapy.Field(output_processor=TakeFirst())
    cover = scrapy.Field(output_processor=TakeFirst())
    specifications = scrapy.Field()
