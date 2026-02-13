import requests
import csv
from bs4 import BeautifulSoup


url = "https://www.dawn.com/"


headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all('h2')
for headline in headlines:
    text = headline.get_text(strip=True)
    if text:
        print(text)


with open("down_news.csv" , "w" , newline="" , encoding= "utf-8"  ) as file:
    writer = csv.writer(file)

    writer.writerow([["Title", "Link"]])


    for h in headline:
        link_tag = h.find('a')
    
            
        if link_tag:
            title = link_tag.get_text(strip=True)
            link = link_tag.get("href")
            
            writer.writerow([title, link])

print("Data successfully saved to dawn_news.csv")