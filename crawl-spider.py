

# Python web crawler for scrapy
# install scrapy :: pip install scrapy
# then type on the command line  scrapy crawl posts


import scrapy


class Webcrawl(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://influencers.quotient.com/blog'
    ]

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'link': post.css('a::attr(href)').get(),
                'title': post.css('.BlogList-item-title::text').get(),
                'date': post.css('time::text').get()
            }
        next_page = response.css('a.BlogList-pagination-link::attr(href)').get()
        next_page = olu + next_page
        print('**************************')
        print(next_page)
        if next_page is not None:
            print('**************************')
            print(next_page)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
