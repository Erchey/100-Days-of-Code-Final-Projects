import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=paracord&viewtype=&tab='
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract product name, price, and reviews
    products = soup.find_all('div', class_='card-info list-card-layout__info')
    data = []
    for product in products:
        name = soup.find('h2', class_='search-card-e-title').text.strip()
        price = soup.find('div', class_='search-card-e-price-main').text.strip()
        reviews = soup.find('div', class_='search-card-e-market-power-common').text.strip().split()[0]

        data.append([name, price, reviews])

    # Save data to a CSV file
    with open('alibaba_products.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price', 'Reviews'])
        writer.writerows(data)
    print('Data saved successfully!')
else:
    print('Failed to fetch the webpage')
