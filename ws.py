import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging
logging.basicConfig(filename="test",level=logging.INFO)
logging.info("Successfully entered log file")
flipkart_url="https://www.flipkart.com/search?q="+"women%20sparx%20sandal&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
client=urlopen(flipkart_url)
menu=bs(client.read(),'html.parser')
links=menu.find_all("a",{"class":"_2UzuFa"})
product_url_list=[]
for i in links:
    product_url_list.append(i['href'])
for i in product_url_list:
    product_url="https://www.flipkart.com"+i
    print(product_url)
    product_page=requests.get(product_url)
    product_page_html=bs(product_page.text,'html.parser')
    comment_section=product_page_html.find_all("div",{"class":"_16PBlm _2RzJ9n"})
    for j in comment_section:
        comment=j.div.div.div.div.div.find_all("div",{"class":"_6K-7Co"})[0].text
    
        print(comment) 
