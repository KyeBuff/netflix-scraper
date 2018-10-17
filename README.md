# Netflix Web Scraper

Built using Python and Scrapy, I followed along with some of the Scrapy docs initially and since then I've just been trying things out. Scrapy has made scraping so accessible, the ability to use CSS selectors to grab data is really useful.

This is one of the many scrapers that will feed the <a href="https://github.com/KyeBuff/flick-api">Flick API</a>.

## Table of Contents
1. [Challenges](#challenges)
2. [What have I learned so far?](#what-have-i-learned-so-far)
2. [What are the next steps?](#what-are-the-next-steps)

## Challenges

### Handling redirects

Netflix will still redirect you if a title has been removed from the platform as old redirects are still in place. I'm handling this by checking the Location header in the response when the Netflix server returns a 301. The condition determines if the redirect will actually go to the title, checking for the string '/title/' and if not it will move onto scraping the next item.

### Duplicate scrapes

The same title can be accessed through different but very similar URLs, so initially I was getting up to 4-5 yields for the same title. I solved this by adding titles to an array, then checking whether the currently scraped item's title already existed in that array and to only process the response if not.

## What have I learned so far?

* How to build a web scraper
* How to handle redirects (301s)
* How to add delays between requests
* How to rotate the user-agent
* How to handle multiple 200s for the same title

## What are the next steps?

* Change this repo so that it can contain all scrapers
* Review alternative approaches to site crawling to improve scraping efficiency
* Setup iterator function to map over the media JSON and post data to the Laravel API
* Build reporting system to handle errors and missing data