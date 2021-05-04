import requests
from bs4 import BeautifulSoup

url1 = "https://www.motorola.com.br/smartphones"
# url2 = "https://www.mibrasil.com.br/celulares/smartphones#/pagina-2"
# url3 = "https://www.mibrasil.com.br/celulares/smartphones#/pagina-3"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response1 = requests.get(url1, headers=header)
# response2 = requests.get(url2, headers=header)
# response3 = requests.get(url3, headers=header)

soup1 = BeautifulSoup(response1.content, "lxml")
# soup2 = BeautifulSoup(response2.content, "lxml")
# soup3 = BeautifulSoup(response3.content, "lxml")

cellphones1 = soup1.findAll("h3")
# cellphones2 = soup2.findAll("h3", class_="name")
# cellphones3 = soup3.findAll("h3", class_="name")

for cellphone in cellphones1:
    print(cellphone.get_text())

# for cellphone in cellphones2:
#     print(cellphone.get_text())
#
# for cellphone in cellphones3:
#     print(cellphone.get_text())