import requests
import bs4
from bs4 import BeautifulSoup ,SoupStrainer

class ImageParser():
    def get_image(self,item_name):
        
        
        url = f'https://steamcommunity.com/market/listings/730/{item_name}'
        
        parse_session = requests.Session()
        get_page = parse_session.get(url)
        parser = BeautifulSoup(get_page.text,'html.parser')
        price = parser.find('div' ,class_='market_listing_largeimage' )
        print(price)
        img = price.img.get('src')
        
        return str(img)

