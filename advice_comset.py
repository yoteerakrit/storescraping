from selenium import webdriver
from bs4 import BeautifulSoup
import helper
import model
import time

def get_av_comset(brands):
    output = []

    for brand in brands:
        # url = "https://www.advice.co.th/product/computer-set/computer-set-brand".replace("brand", brand)
        url = "https://www.advice.co.th/product/computer-set/computer-set-intel"

        driver = webdriver.Chrome() 
        # res = helper.get_request(url)

        driver.get(url)

        time.sleep(5)

        # soup = BeautifulSoup(res.content, 'html.parser')
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        items = soup.find('div', class_="product-column-4").find_all('div', class_="item")
        
        print(len(items))

        for item in items:
            # brands = item['item-brand']
            title = item['item-name']

            info = item.find('div', class_="item-spec")
            # full_price = item.find('div', class_="price-to-cart").find('div', class_="sale")
            price = item.find('div', class_="online-btn-cart")['data-price']
            full_price = item.find('div', class_="online-btn-cart")['data-price_srp']
            discount = item.find('div', class_="online-save")

            discount_text = ''
            if discount is not None:
                discount_text = discount.text.replace('ประหยัด', '').replace('.-', '').strip()

            stock_info=""
            if not item.find('div', class_="sales-price") and not item.find('div', class_="cart-srp"):
                stock_info = "out of stock"

            title_text = ""
            if title is not None:
                title_text = title.strip()

            info_text = ""
            if info is not None:
                info_text = info.text.strip()

            # full_price_text = ""
            # if full_price is not None:
            #     full_price_text = full_price.text.strip()

            output.append(model.computer_info(brand.upper() ,title_text, info_text, price, full_price, discount_text, stock_info))
            

    return output