import requests
import pandas as pd
from bs4 import BeautifulSoup

page = 1
all_quotes = []

while True:
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    
    quotes = soup.find_all("div", class_="quote")
    if not quotes:
        break  # No more pages

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        all_quotes.append({"quote": text, "author": author})

    page += 1

df = pd.DataFrame(all_quotes)
df.to_csv("quotes.csv", index=False)
print("Scraping completed. Quotes saved to quotes.csv")