Introduction
=============

Tax clock scraper is a combination of scrapers. These scrapers obtain data from media houses' websites in Kenya.

This data includes  the trending news in the countries business sector. 

Web scraping or crawling is the technique for gathering data or information on web pages by downloading and parsing the HTML code to extract the data you want.

Since most websites don't offer API’s for getting data from , web scraping can be the only solution when it comes to extracting website information.  Lots of companies use it to obtain data from other websites.

Almost everything can be extracted from HTML, the only information that are 'difficult' to extract are inside images or other medias.


Features
---------

* Data is obtained from several media houses. The properties of the data include image, link and title.The scraper gets data from the following sites:

   	* `Standard Media <https://www.standardmedia.co.ke/business/category/19/business-news>`_
	* `Nation Media <http://www.nation.co.ke/business/corporates/1954162-1954162-u0riql/index.html>`_
	* `The Star Media <http://www.the-star.co.ke/sections/business_c29663>`_
	* `Capital Media <http://www.capitalfm.co.ke/business/section/kenya>`_

* Data storage locally in a json file and online in amazon s3 webservice.

* Sorting data obtained online by the date the data was published.

* Sending slack messages to a slack channel in case of error or s3 downtime.

Project Background
-------------------

Taxclock scraper is part of the code for Africa projects that gets data online. This information can be found in their taxclock website .

Implementation Notes
----------------------

* The application is implemented using python language. Python is a powerful language and its support for OOP makes it even more robust. The scrapers are implemented using the concept of OOP. The base scraper contains all the methods that are common among the other scrapers. The other scrapers inherit from this scraper.

* The key library for obtaining data is beautiful soup. The main reason for using the library is its ability to parse html content. From the parsed html content its easy to get any information stored in the html tags.
