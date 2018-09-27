import scrapy

class MediaSpider(scrapy.Spider):
    # Sub class scrapy.Spider

    # Name which identifies spider, must be unique
    name = "media"

    starting_title_n = 80117552
    handle_httpstatus_list = [404]
    # dont_redirect = False

    # Variab;e read my spider sub class which is iterated over to create a request on each item
    start_urls = [
        'https://www.netflix.com/title/' + str(starting_title_n),
    ]

    # Function will run to parse responses
    def parse(self, response):
        self.starting_title_n += 1
        next_page = 'https://netflix.com/title/' + str(self.starting_title_n+1)

        if response.status == 200:                  
            genres = response.css('.genre-list::text').extract_first().strip('')
            yield {
                'title': response.css('h1.show-title::text').extract_first(),
                'synopsis': response.css('p.synopsis::text').extract_first(),
                'img_url': response.css('img.title-hero-image::attr("src")').extract_first(),
                'isFilm': genres.lower().find('film') > -1,
                'genres': genres,
                'apps': ["Netflix"],
            }
            yield response.follow(next_page, callback=self.parse)
