#import requests
#from bs4 import BeautifulSoup
#import re
#import time
#from datetime import datetime, timedelta
#import json
#from urllib.parse import urljoin
#import urllib.request


#url = 'https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1'
#data = []

#r=requests.get(url)
#r.text
#soup = BeautifulSoup(r.text, 'lxml')
#z = soup.find('span', class_='long_title description').find('a', class_='plttl').get('href')
#x = soup.find('span', class_='long_title description').find('a', class_='plttl').text
##y = soup.find('a', class_='plttl')

##ret = soup.find('div', class_='s1')
##print(ret)

##get name
#soup.find('a', class_='plttl').text
#print(name)

##get url
#soup.find('span', class_='long_title description').find('a', class_='plttl').get('href')
##print(awer)

##get price
#price = soup.find('div', class_='price').text
##print(price)


##regex = re.compile(r'^\s*([\d.].*+)')
##m = regex.match(text)
##if m:
    ##screen_size = m.groups(1)

##rew = soup.find('span', class_='long_title description')
##print(rew)

##all links
#lawer = soup.find('span', class_='long_title description').find('a', class_='plttl').get('href')
##link to lenovo
#pawer = soup.find( href = re.compile('https://www.jarcomputers.com/lenovo'))


##for index, value in enumerate(pawer):
    ##print("At index {}, value is {}".format(index, value))

#laptops = soup.find_all('span', class_='long_title description')

##for laptop in laptops:
    ##name = laptop.text
    ###price = laptop.find('div', class_='price').text
    
    ##data.append(name)
##names=[]  
##laptop_names = soup.find_all( href = re.compile('lenovo'))
##for laptop_name in laptop_names:
    
    ##if laptop_name not in names:
        ##names.append(laptop_name)
       
##print(*names, sep = '\n')
##print(len(names))
##print()

import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime, timedelta
import json
from urllib.parse import urljoin


class LaptopsLenovo:
    # constract
    def __init__(self, brand, price, screen_size):
        self.brand = brand
        self.price = price
        self.screen_size = screen_size

    def brand(self, text: str) -> str:
        regex = re.compile()
        pass

    def price(self):
        price = soup.find('div', class_='price').text
        pass

    def screen_size(self, text: str) -> float:
        regex = re.compile(r'^\s*([\d.].*+)')
        m = regex.match(text)
        if m:
            screen_size = m.groups(1)
            pass


data = []

url = 'https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1'
r = requests.get(url)
r.text
soup = BeautifulSoup(r.text, 'lxml')
z = soup.find('span', class_='long_title description').find('a', class_='plttl').get('href')
x = soup.find('span', class_='long_title description').find('a', class_='plttl').text
# y = soup.find('a', class_='plttl')

ret = soup.find('div', class_='s1')
# print(ret)

# get name
name = soup.find('a', class_='plttl').text
print(name)

# get url
awer = soup.find('span', class_='long_title description').find('a', class_='plttl').get('href')
lenovo_link = soup.find_all(href=re.compile('lenovo'))
# print(lenovo_link)

# get price
price = soup.find('div', class_='price').text
print(price)

#  Print all laptop names
laptop_names = soup.find_all( href = re.compile('lenovo'))
for laptop_name in laptop_names:
    print(laptop_name.text.strip())

# Print all laptop prices
laptop_prices = soup.select('.price')
for laptop_price in laptop_prices:
    print(laptop_price.text.strip())




if __name__ == 'main':
    url = 'https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1'
    