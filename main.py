from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

page = 40
product_names = []
product_prices = []
for i in range(1, int(page) + 1):
    url = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&p%5B%5D=facets.brand%255B%255D%3DHP&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkhQIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_12.metroExpandable.METRO_EXPANDABLE_HP_gaming-laptops-store_DUA3GDGO4GNV_wp7&fm=neo%2Fmerchandising&iid=M_a07f52db-a7f2-4f11-83bc-1b544cc98ec4_12.DUA3GDGO4GNV&ppt=clp&ppn=laptops-store&ssid=pi2rwt3bu80000001685828496875'+ str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    names = soup.find_all('div',class_="_4rR01T")
    prices = soup.find_all('div',class_="_30jeq3")

    for name, price in zip(names, prices):
        product_names.append(name.text)
        product_prices.append(price.text)

df = pd.DataFrame({'Name': product_names, 'Price': product_prices})
file_path = 'feproduct.csv'
if os.path.isfile(file_path):
    df.to_csv(file_path, mode='a', header=False, index=False)
else:
    df.to_csv(file_path, index=False)

print("CSV file saved successfully.")