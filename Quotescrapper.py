from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        q=quote.find('span',class_='text').text
        w=quote.find('small',class_='author').text
        print(f"{'Quote':5}: {q}")
        print(f"{'Writer':5}: {w}")


else:
    print("Error")
