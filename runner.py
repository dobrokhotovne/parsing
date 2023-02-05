from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

from kino_parser.spiders.kinometro import KinometroSpider

if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    search = []

    count = input('Enter periods count for parsing (1 - 30): ') #запрос пользователю на ввод количество периодов, с проверкой на ввод числа
    while not type(count) == int:
        try:
            count = int(count)
            if count < 1 or count > 30:
                count = (input('!!!ERROR!!! Enter periods count for parsing (1 - 30, digits only): '))
        except ValueError:
            count = (input('!!!ERROR!!! Enter periods count for parsing (1 - 30, digits only): '))

    for i in range(count): #запрос пользователю на ввод месяца и года, с проверкой на ввод числа
        month = input(f'Enter month for {i + 1} period  (1 - 12): ')
        while not type(month) == int:
            try:
                month = int(month)
                if month < 1 or month > 12:
                    month = (input(f'!!!ERROR!!! month for {i + 1} period  (1 - 12, digits only): '))
            except ValueError:
                month = (input(f'!!!ERROR!!! month for {i + 1} period  (1 - 12, digits only): '))

        year = input(f'Enter year for {i + 1} period  (2007 - 2033): ')
        while not type(year) == int:
            try:
                year = int(year)
                if year < 2007 or year > 2033:
                    year = (input(f'!!!ERROR!!! Enter year for {i + 1} period  (2007 - 2033, digits only): '))
            except ValueError:
                year = (input(f'!!!ERROR!!! Enter year for {i + 1} period  (2007 - 2033, digits only): '))

        search.append([month, year])

    runner.crawl(KinometroSpider, search=search)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
