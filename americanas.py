import requests
from bs4 import BeautifulSoup

url = "https://www.americanas.com.br/busca/celular?chave_search=acterm&limit=72"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

name = soup.findAll("span", class_="src__Text-sc-154pg0p-0 src__Name-sc-1k0ejj6-3 dSRUrl")
price = soup.findAll("span", class_="src__Text-sc-154pg0p-0 src__PromotionalPrice-sc-1k0ejj6-7 iIPzUu")

for n in range(len(name)):
    print(name[n].get_text())
    print(price[n].get_text())