''' Chapter 1 - illustrates several equivalent methods to scrape info from a webpage

import requests
import urllib3
from bs4 import BeautifulSoup



url = 'https://www.python.org/events/python-events'


Using requests

#req = requests.get(url)

using urllib3

req = urllib3.PoolManager()
res = req.request('GET', url)



Beautiful soup parses the HTML

#requests version
#soup = BeautifulSoup(req.text, 'lxml')
#urllib3 version
soup = BeautifulSoup(res.data, 'html.parser')





events = soup.find('ul', {'class': 'list-recent-events'}).findAll('li')

for event in events:
    event_details = dict()
    event_details['name'] = event.find('h3').find('a').text
    event_details['location'] = event.find('span', {'class', 'event-location'}).text
    event_details['time'] = event.find('time').text
    print(event_details)



'''
''' The scrapy version '''

import scrapy
from scrapy.crawler import CrawlerProcess

class PythonEventsSpider(scrapy.Spider):
    name = 'pythoneventsspider'

    start_urls = ['https://python.org/events/python-events/',]
    found_events = []

    def parse(self, response):
        print(response)

        for event in response.xpath('//ul[contains(@class, "list-recent-events"]/li'):
            event_details = dict()
            event_details['name'] = event.xpath('h3[@class="event-title"]/a/text()'.extract_first())
            event_details['location'] = event.xpath('p/span[@class="event-location"]/text()'.extract_first())
            event_details['time'] = event.xpath('/p/time/text()'.extract_first())
            self.found_events.append(event_details)


if __name__ == "__main__":
    process = CrawlerProcess({'LOG_LEVEL':'ERROR'})
    process.crawl(PythonEventsSpider)
    spider = next(iter(process.crawlers)).spider
    process.start()

    for event in spider.found_events: print(event)