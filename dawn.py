import requests
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


