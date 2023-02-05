import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient


class KinoParserPipeline: #PipeLine, записывающий item  в базу данных Mongo
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.movies

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        collection.insert_one(item)
        print()
        return item

class KinoCoverPipeline(ImagesPipeline): #Pipeline для скачивания фотографий
    def get_media_requests(self, item, info):
        if item.get('cover'):
            img = f"https://www.kinometro.ru{item.get('cover')}"
            try:
                yield scrapy.Request(img)
            except Exception as e:
                print(e)

    def item_completed(self, results, item, info):
        print()
        if results:
            item['cover'] = [itm[1] for itm in results if itm[0]]
        return item


class KinoSpecPipeline: #Pipeline - обработчик поля specificationsб приведение из списка к словарю
    def process_item(self, item, spider):
        if item.get('specifications'):
            specs = {}
            i = 0
            while i < len(item['specifications']):
                specs[item['specifications'][i]] = item['specifications'][i+1]
                i+=2
        item['specifications'] = specs
        return item