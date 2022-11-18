# SearchForApartments
This script assist people looking for new apartments by scrapping pages and getting links from the code

# Requirements

1) Install the required Python libraries
$ pip3 install -r requirements.txt

2) Create a configuration.yml in the project root folder based on the configuration.sample.yml file

3) Create a Telegram BOT and set the Token in the configuration.yml file

4) Initiate oe or many chats with the Telegram BOT and get the chat-id from each chat, so you could use them in the configuration.yml file

5) Set the database name in the configuration.yml, like "db1.db" or whatever you like

6) For each page you would like to scrap, fill the following information:
- Web: the URL including uriParams and queryParams you would like to scrap
- Element: identify which HTML element (div, p, h1, h2, etc.) contains the "<a href" to the scrapped link
- Class: the class id that is used in the configured element 
- SitePrefix: in case the href link points to a url without domain, you may add the domain as a prefix

Example:
Web: "https://www.apartments.com/new-york-ny/low-income/"

Analyzing the response, we find the following link:
<header class="placard-header has-logo">
	<div class="property-information">
		<a class="property-link" href="https://www.apartments.com/riverton-square-new-york-ny/yd8wsxt/" aria-label="Riverton Square, New York, NY">
			<div class="property-title" title="Riverton Square, New York, NY">
				<span class="js-placardTitle title">Riverton Square</span>
			</div>
			<div class="property-address js-url" title="2225-2265 5th Ave, New York, NY 10037">2225-2265 5th Ave, New York, NY 10037</div>
		</a>
	</div>
</header>

So...
Element: "div"
Class: "property-information"
SitePrefix: ""

# Usage
cd /folder_location

python3 main.py

## Disclaimer
This example is provided as a reference for your own usage and is not to be considered my own product.
By using it, you are approving the license from different products and regulations like CloudScrapper, BeautifulSoup4, Requests, lXML, PyYaml and more.
This article involves products and technologies which do not form part of my catalog. Technical assistance for such products is limited to this repository.
