Error Handling
===============

Every application needs to have a good way to capture errors. Errors are bound to occur during the application lifecycle. 

It is good to have these errors logged somewhere to help developers figure out the issue quickly especially the maintenance team.

Taxclock scraper captures errors by logging them to a file and sending slack messages to slack.

Sending slack messages is achieved using slack webhook. 


Logging is achieved using: 

	``python logging``
	