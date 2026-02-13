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

with open("dawn_full_news.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link", "Content"])

    for h in headlines:
        link_tag = h.find("a")
        if link_tag:
            title = link_tag.get_text(strip=True)
            link = link_tag.get("href")

            # Agar link relative ho
            if link.startswith("/"):
                link = base_url + link

            # Ab article page open karenge
            article_response = requests.get(link, headers=headers)
            article_soup = BeautifulSoup(article_response.text, "html.parser")

            paragraphs = article_soup.find_all("p")

            content = ""
            for p in paragraphs:
                content += p.get_text(strip=True) + " "

            writer.writerow([title, link, content])

            print("Saved:", title)

            time.sleep(1)  

print("Full articles saved successfully!")