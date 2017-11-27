Testing
========

Scraping websites is a very dynamic process. Design changes regularly, anytime the scraper can fail due to change in the tag it uses to get data from. Therefore, it is good to write tests for any application. 

The scraper has some tests for checking whether the tags  being used to scrape the sites are still the ones in the website html content. 
If you run the tests and any of them fails and it  checks for a tag there is need to revisit the website and check the new tag holding the data. The main reason for the tests is to check whether your code is working as expected.

To run tests:

Run the command below in your root folder.

	``nosetests -v``

**Scraper Tests**

    .. automodule :: taxclock.tests.test_scrapers
        :members:

**Configuration Tests**

    .. automodule :: taxclock.tests.test_config
        :members: