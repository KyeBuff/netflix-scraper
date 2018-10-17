import scrapy

from scrapy.spider import Spider

class MediaSpider(scrapy.Spider):
    # Sub class scrapy.Spider

    # Name which identifies spider, must be unique
    name = "media"
    rotate_user_agent = True

    starting_title_n = 80117552
    handle_httpstatus_list = [301, 302, 404]
    already_scraped = []
    dont_filter=True

    # Variab;e read my spider sub class which is iterated over to create a request on each item
    start_urls = [
        'https://www.netflix.com/title/' + str(starting_title_n),
    ]

    # Function will run to parse responses
    def parse(self, response):
        if response.status == 404:
            self.starting_title_n += 1
            next_page = 'https://netflix.com/title/' + str(self.starting_title_n+1)
            yield response.follow(next_page, callback=self.parse)

        if response.status == 301:   
            redirect_url = str(response.headers['Location']).replace("'", "")[1:]
            # self.redirect_attempts += 1
            if redirect_url.find('title') > -1:
                self.starting_title_n += 1
                yield response.follow(redirect_url, callback=self.parse)
            else:
                self.starting_title_n += 1
                next_page = 'https://netflix.com/title/' + str(self.starting_title_n+1)
                yield response.follow(next_page, callback=self.parse)

        if response.status == 200:
            genres = response.css('.genre-list::text').extract_first()

            if response.css('h1.show-title::text').extract_first() not in self.already_scraped:
                yield {
                    'title': response.css('h1.show-title::text').extract_first(),
                    'synopsis': response.css('p.synopsis::text').extract_first(),
                    'img_url': response.css('img.title-hero-image::attr("src")').extract_first(),
                    'isFilm': genres.lower().find('film') > -1 if genres else True,
                    'genres': genres.strip('').split(',') if genres else [],
                    'apps': ["Netflix"],
                }

            self.already_scraped.append(response.css('h1.show-title::text').extract_first())

            self.starting_title_n += 1

            next_page = 'https://netflix.com/title/' + str(self.starting_title_n)
            yield response.follow(next_page, callback=self.parse)
