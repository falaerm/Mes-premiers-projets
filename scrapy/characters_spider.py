import scrapy

class BlogSpider(scrapy.Spider):
    name = 'characterspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Catégorie:Personnage_d%27animation']

    def parse(self, response):
        for link in response.css('iv#mw-pages div.mw-content-ltr li'):
            yield {'character': title.css('a ::text').extract_first()}