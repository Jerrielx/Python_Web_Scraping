# Project:  Web Scraping
# Date:     2025-11-26
# Author:   Jerry Cheung
# File:     scraper1.py
# Description:  Basic web scraping with python


from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0"}
page_to_scrape = requests.get("http://quotes.toscrape.com", headers=headers)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    
print(page_to_scrape.status_code)
print(len(page_to_scrape.text))
