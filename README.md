## Taxclock Kenya News Scraper

To give context to the [Kenya's TaxClock](https://taxclock.codeoforkenya.org/), we are scraping the business headlines from Kenya's major news sites to display on the TaxClock Website.

<!-- TODO: Insert screenshot of the headlines -->

The scraper get data from the following websites:
* Standard Media :https://www.standardmedia.co.ke/business/category/19/business-news
* Nation Media :http://www.nation.co.ke/business/corporates/1954162-1954162-u0riql/index.html
* The Star Media: http://www.the-star.co.ke/sections/business_c29663
* Capital Media: http://www.capitalfm.co.ke/business/section/kenya

For more detailed documentation on how this scraper works, check out the docs [here](http://taxclock-news.readthedocs.io/en/ch-project-documentation/introduction.html)

---

## Getting started.

#### How the scraper works

 * Each website has it's own scraper. This is because sites are designed differently.
 * The python library that this scraper uses is beautiful soup. 
 * Beautiful soup generates a result set containing the html content of the site url passed to it.
 * With the html content you can retrieve the data that you want. 
 * It is necessary to understand html tags to be able to unpack data from the websites.
 * For the scrapers in this project, each scraper gets data from a div tag that contains the data.
 * Since the data is dynamic and in different formats, there is need to get the html tags of the data that you want.
 * Taxclock needs the stories with the properties link, image, title and date the story was published.
 * The html tags for the properties are a(from this we get the href),img (from this we get the src) and h(1-6)-this gives us text  for the date and title.

 * After obtaining this data there is need to store it. In our case we store it in a file locally and cloud storage(amazon webservice). You can read more on amazon webservices and how they work [here](https://aws.amazon.com/s3/).

<!-- TODO: Talk a bit more about the archiving process -->

## Installation

Clone the repository, enter the directory, and install the project dependencies:

```sh
$ git clone https://github.com/CodeForAfrica-SCRAPERS/taxclock_ke_news.git
$ cd taxclock_ke_news
$ pip install -r requirements.txt
```

<!-- TODO: Add steps for virtualenv -->

Before you run the project ensure you have the following environment variables set in your virtual environment.

```sh
$ export MORPH_AWS_ACCESS_KEY=<aws_access_key>
$ export MORPH_AWS_SECRET_KEY=<aws_secret_key>
$ export TIMEOUT=<default_timeout>
$ export MORPH_WEBHOOK_SLACK= <webhook_url>
```

We're now ready to run the scraper and scrape the headlines from the sites:

```sh
$ python scraper.py
```

### Storage

The scraper can either store the data locally in a `data` folder or on S3 for easy access.


## Error Handling

The application captures errors by logging them to a file and sending slack messages to slack.

Logging is achieved using Python's `logging` module.

Sending slack messages is achieved using the library `slack_log_handler`.


## Tests

Scraping websites is a very dynamic process. Sites' design change regularly. This means, anytime the scraper can fail due to change in the div it uses to get data from. This is the main reason for writing  tests.

We have some tests for checking whether the div tag that is being used to scrape the site is still the one in the website html content. If you run the tests and any of them fails and it  checks for a div there is need to revisit the website and check the new div holding the data. The main reason for tests is to check whether your code is working as expected.

To run tests, run the command below in your root folder:
```
$ nosetests -v
```

# License

MIT License