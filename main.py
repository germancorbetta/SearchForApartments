import cloudscraper
from bs4 import BeautifulSoup
import functions

links = []

functions.CreateLinksTable()
sites = functions.loadSites()
print("-"*20)

for site in sites:
    siteName = site
    siteUrl = sites[site]["web"]
    siteElement = sites[site]["element"]
    siteClass = sites[site]["class"]
    sitePrefix = sites[site]["sitePrefix"]

    scraper = cloudscraper.create_scraper(disableCloudflareV1=True) 
    request = scraper.get(siteUrl)

    # Extract links from the response
    if (request.status_code != 200):
        print(siteName + ": HTTP request error")
    elif (request.status_code == 200):
        page_content = BeautifulSoup(request.text, 'lxml')
        properties = page_content.find_all(siteElement, class_=siteClass)
        for prop in properties:
            for link in prop.findAll('a'):
                href = link.get('href')
                hasHash = href.find('#',1,len(href))
                if hasHash == -1:
                    links.append(sitePrefix + href)
                else:
                    unClearLink = href
                    links.append(sitePrefix + unClearLink[0:unClearLink.find('#',1,len(unClearLink))])

        if(len(links) == 0):
            print(siteName + ": No links in the response")


    # For each link, verify if it exists in the database, otherwise send the notification and add it in the DB
    for link in links:
        if (not functions.LinkExists(link)):
            print("Sending: " + link)
            functions.sendToTelegram("Nuevo depto en " + siteName + ": " + link)
            functions.InsertLink(link)

    print(siteName + " finished")
    print("-"*20)
