import requests
import bs4
from bs4 import BeautifulSoup ,SoupStrainer

class CsgoFloat_api_request():

    def __init__(self, inspect_link):

        self.inspect_link = inspect_link
        self.buy_price = 0
        self.float_id = None
        self.item_history = None
        self.parser = None
        self.item_name = None
        self.floatvalue = None
        
    def get_parser(self):
        reqest_url = f'https://api.csgofloat.com/?url={self.inspect_link}' 
        parse_session = requests.Session()
        proxies = { 'http' : 'http://tgmkycle:rg36ssxcn25g@188.74.210.207:6286' } 
        get_page = parse_session.get(reqest_url, proxies=proxies)
        get_page.text
        parser = BeautifulSoup(get_page.text,'html.parser')
        parser = str(parser)
        self.parser = parser.split(",")

    def get_float_id(self):
        self.get_parser()
        
        for i in range(len(self.parser)): 
           if '"floatid":' in self.parser[i]:
                float_pos = i

        self.float_id = self.parser[float_pos].split(":")[1].replace('"','')
        #print(self.float_id) 
        
        return self.float_id

    def get_item_history(self,saved_id = None):
        if(saved_id):
            self.float_id = saved_id
            #print(f"saved f_id {self.float_id}")
        else:
            self.get_float_id()

        url = f"https://csgofloat.com/api/v1/floatdb/item/{self.float_id}/history"
        headers = {'Authorization': '3AV08BVJIpt17v8894-Rt0GhV2oS3C0y'}
        self.item_history = requests.get(url, headers=headers).text
        #print(self.item_history)

        return self.item_history

    def get_price(self, float_id = None):
        
        if(float_id):
            self.get_item_history(saved_id = float_id )
        else:
            self.get_item_history()

        parser = self.item_history.split(",")
        #print(parser)
        for i in range(len(parser)): 
             if 'price' in parser[i]:
                 price_pos = i
        
        if "price_pos" in locals():   
             try:
                    self.buy_price = parser[price_pos].split(":")[1]
                    self.buy_price = float(self.buy_price) / 100
             except:
                    self.buy_price = parser[price_pos].split(":")[2]
                    self.buy_price = float(self.buy_price) / 100
        else:
                print("Price error !")

        print(self.buy_price)
       
        return self.buy_price

    def get_item_name(self):
        if(self.parser != None):
             print("parser loaded")
             for i in range(len(self.parser)): 
                if '"full_item_name":' in self.parser[i]:
                    name_pos = i
             
             if "name_pos" in locals():
                 self.item_name = self.parser[name_pos].split(":")[1].replace('"','')
                 self.item_name = self.item_name.replace('}}','')
        else:
            print("parser NOT loaded")
            self.get_parser()
            for i in range(len(self.parser)): 
                if '"full_item_name":' in self.parser[i]:
                    name_pos = i
             
            if "name_pos" in locals():
                 self.item_name = self.parser[name_pos].split(":")[1].replace('"','')
                 self.item_name = self.item_name.replace('}}','')

        print(self.item_name)
        return self.item_name

    def get_floatvalue(self):
        if(self.parser != None):
             print("parser loaded")
             for i in range(len(self.parser)): 
                if '"floatvalue":' in self.parser[i]:
                    float_pos = i
             
             if "float_pos" in locals():
                 self.floatvalue = self.parser[float_pos].split(":")[1].replace('"','')
                 
        else:
            print("parser NOT loaded")
            self.get_parser()
            for i in range(len(self.parser)): 
                if '"floatvalue":' in self.parser[i]:
                    float_pos = i
             
            if "float_pos" in locals():
                 self.floatvalue = self.parser[float_pos].split(":")[1].replace('"','')

        #print(self.floatvalue)
        return self.floatvalue


                 
        




                 
            
        



    




#api = CsgoFloat_api_request("steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M4199075303852538710A28096751896D2741753664238999498")
  
#api.get_price()
#api.get_item_name()
#api.get_floatvalue()


