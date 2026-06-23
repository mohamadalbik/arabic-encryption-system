from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd

all_poems = []

for i in range(1, 6):
    try:
        URL = f"https://www.aldiwan.net/quote-Topics-%D8%B1%D9%88%D9%85%D9%86%D8%B3%D9%8A%D8%A9?page={i}"  # Added f-string
        print(f"Scraping page {i}: {URL}")
        response = requests.get(URL, timeout=100)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        for poem in soup.find_all('div', class_='p-3 mb-2 d-flex flex-column quote'):
            verses = [p.text.strip() if p.text is not None else '\n' for p in poem.find_all('p')]
            category = poem.find(
                'a', class_='btn btn-primary px-4 py-1 sm-border-btn sm-white-btn'
            ).text.strip()
            all_poems.append({"category": category, "verses": verses})

        sleep(1)

    except Exception as e:
        print(f"Error on page {i}: {str(e)}")
        continue


df = pd.DataFrame(all_poems)


df.to_csv("database/arabic_poems_romance.csv", index=False, encoding='utf-8-sig')
print("Scraping completed. Data saved to arabic_poems.csv")
