Getting started
================
In any project it's good to understand how the application works. This is key in helping one get up and running with a new code base.

General Overview
-----------------
A general overview of the application. A quick guide to help grasp how taxclock scraper was achieved.

    * Each website has it's own scraper. This is because sites are designed differently.

    * The python library that this scraper uses is beautiful soup. 

    * Beautiful soup generates a result set containing the html content of the site url passed to it.

    * With the html content you can retrieve the data that you want. 

    * It is necessary to understand html tags to be able to unpack data from the websites.

    * For the scrapers in this project, each scraper gets data from a div tag that contains the data.

    * Since the data is dynamic and in different formats, there is need to get the html tags of the data that you want.

    * Taxclock needs the stories with the properties link, image, title and the date the story was published.

    * The html tags for the properties are a(from this we get the href),img (from this we get the src) and h(1-6)-this gives us text  for the date and title.

    * After obtaining this data there is need to store it. In our case we store it in a file locally and cloud storage(amazon webservice). You can read more on amazon webservices and how they work `here <https://aws.amazon.com/s3/>`_.



Scrapers
---------

**Base Scraper**

    .. automodule :: taxclock.scrapers.base
        :members:

**Capital Media Scraper**

    .. automodule :: taxclock.scrapers.capital
        :members:

**Nation Media Scraper**
 
    .. automodule :: taxclock.scrapers.nation
        :members:

**Standard Media Scraper**

    .. automodule :: taxclock.scrapers.standard
        :members:

**The Star Media Scraper**

    .. automodule :: taxclock.scrapers.the_star
        :members:
