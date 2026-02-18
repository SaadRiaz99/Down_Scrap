import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import time
from datetime import datetime, timedelta

# Base URL
base_url = "https://www.dawn.com/"


headers = {"User-Agent": "Mozilla/5.0"}


csv_file = "dawn_last_30_days.csv"
writer = None


with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Title", "Link", "Content"])

    
    for i in range(30):
        date_obj = datetime.now() - timedelta(days=i)
        date_str = date_obj.strftime("%Y-%m-%d")
        archive_url = f"https://www.dawn.com/archive/{date_str}"

        print("Scraping:", archive_url)
        try:
            response = requests.get(archive_url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

           
            articles = soup.select("h2.story__title a")

            for article in articles:
                title = article.get_text(strip=True)
                link = urljoin(base_url, article.get("href"))

             
                try:
                    article_response = requests.get(link, headers=headers)
                    article_soup = BeautifulSoup(article_response.text, "html.parser")
                    paragraphs = article_soup.select("div.story__content p")
                    content = " ".join([p.get_text(strip=True) for p in paragraphs])

                    
                    writer.writerow([date_str, title, link, content])
                    print("Saved:", title)

                    time.sleep(1)  #

                except Exception as e:
                    print("Article Error:", e)

            time.sleep(1)  

        except Exception as e:
            print("Archive Error:", e)

print("All data saved in", csv_file)
