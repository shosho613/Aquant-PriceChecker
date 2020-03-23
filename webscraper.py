from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from file_reader import file_reader
import time

class webscraper(object):
    
    def __init__(self,filename):
        self.file_reader = file_reader(filename)
        self.products = self.file_reader.products
        self.driver = webdriver.Chrome("./chromedriver_version_80")

    def search_for(self, item_name):
        try:
            search_bar = self.driver.find_element_by_name("searchText")
            search_bar.clear()
            search_bar.send_keys(item_name)
            search_bar.send_keys(Keys.RETURN)
            print(self.driver.current_url)
        except:
            print("in except")
            search_bar = self.driver.find_element_by_name("searchText")
            search_bar.clear()
            search_bar.send_keys(item_name)
            search_bar.send_keys(Keys.RETURN)
            print(self.driver.current_url)
    
    def find_price(self, item_name):
        self.driver.get("https:/www.supplyhouse.com")

        d = dict()
        price_toreturn = "p"
        url_toreturn = "u"
        self.search_for(item_name)
        try:  
            WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "rec_1")
            )).click()
       
            price = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.NAME, "unit-price-text")
            ))
            print(price.text)
            price_toreturn = price.text
            url_toreturn = self.drive.current_url
           
        except:
            print("Price not found")
            price_toreturn = "Price not found"
            url_toreturn = ""
        d['price'] = price_toreturn
        d['url'] = url_toreturn
        return d


    def run_price_finder(self):
        #self.driver.get("https:/www.supplyhouse.com")
        prices = []
        urls = []
        for index, product_name in self.products.iterrows():
            if index == 100:
                break
            d = self.find_price(product_name)
            if d['price'] != None:
                prices.append(d['price'])
                urls.append(d['url'])
            else:
                prices.append("Price not found")
                urls.append("")
        self.driver.close()
        self.driver.quit
        print(prices)
        print(urls)
        self.file_reader.df["Prices"] = prices
        self.file_reader.df["URLs"] = urls
        print(self.file_reader.df.header())
    
    
def main():
    wb = webscraper("hussmann.com.xlsx")
    d = wb.find_price("IGNITOR CARRIER")
    print(d)
    #wb.run_price_finder()


if __name__ == "__main__":
    main()