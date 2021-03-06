# Netflix Web Scraper
**STILL IN DEVELOPMENT**

This is one of the many scrapers that will feed the <a href="https://github.com/KyeBuff/flick-api">Flick API</a>.

Built using Python and Scrapy, I followed along with some of the Scrapy docs initially and since then I've just been trying things out. Scrapy has made scraping so accessible, the ability to use CSS selectors to grab data is really useful.

## Table of Contents
1. [Challenges](#challenges)
2. [What have I learned so far?](#what-have-i-learned-so-far)
3. [What are the next steps?](#what-are-the-next-steps)
4. [Setup](#setup)

## Challenges

### Handling redirects

Netflix will still redirect you if a title has been removed from the platform as old redirects are still in place. I'm handling this by checking the Location header in the response when the Netflix server returns a 301. The condition determines if the redirect will actually go to the title, checking for the string '/title/' and if not it will move onto scraping the next item.

### Duplicate scrapes

The same title can be accessed through different but very similar URLs, so initially I was getting up to 4-5 yields for the same title. I solved this by adding titles to an array, then checking whether the currently scraped item's title already existed in that array and to only process the response if not.

## What have I learned so far?

* How to build a web scraper
* How to handle redirects and 404s
* How to add delays between requests
* How to rotate the user-agent
* How to handle multiple 200s for the same title

## What are the next steps?

* Change this repo so that it can contain all scrapers
* Review alternative approaches to site crawling to improve scraping efficiency
* Setup iterator function to map over the media JSON and post data to the Laravel API
* Build reporting system to handle errors and missing data

## Setup

You will need to have both Python's package manager <a href="https://pip.pypa.io/en/stable/installing/">pip</a> and <a href="https://doc.scrapy.org/en/latest/intro/install.html">virtualenv</a> installed.

```
mkdir nf-scraper && cd nf-scraper
```

Creates the virtual environment where Scrapy can operate.
```
virtualenv ENV && cd ENV
```

```
git clone git@github.com:KyeBuff/netflix-scraper.git
```

```
pip install scrapy
```

```
source bin/activate
```

Then you can run the scraper using:

```
cd netflix-scraper/nfScraper/ && scrapy crawl -o media.json media
```