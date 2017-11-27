Installation.
=============
To get the application up and running on your machine.

* Clone the repository using the link.

	`Taxclock <https://github.com/CodeForAfrica-SCRAPERS/taxclock_ke_news.git>`_

* Navigate to the folder.

	``taxclock_ke_news``

* Install the project dependencies by running the command below on your terminal. 

	``pip install -r requirements.txt``

* Before you run the project ensure you have the following environment variables set in your virtual environment.

	.. code-block:: python

		export MORPH_AWS_ACCESS_KEY=<aws_access_key>

		export MORPH_AWS_SECRET_KEY=<aws_secret_key>

		export TIMEOUT_TIME=<default_timeout>

		export MORPH_WEBHOOK_SLACK= <webhook_url>


* After the above steps and everything is set.

	Run ``python scraper.py`` . 

* After running the command you will get data from the websites. For visual view of the data you need to alter the s3 to have data stored in a local file. The logic behind it is that if the S3 is down then store the data in a local file.
