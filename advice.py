from bs4 import BeautifulSoup
import helper
import model

def get_av(type, brands):
    output = []

    for brand in brands:
        url = "https://hwantest.advice.co.th/product/type/type-brand".replace("type", type).replace("brand", brand)
        res = helper.get_request(url)

        soup = BeautifulSoup(res.text, 'html.parser')

        items = soup.find('div', class_="product-column-4").find_all('div', class_="item")

        for item in items:
            # brands = item['item-brand']
            title = item['item-name']

            info = item.find('div', class_="item-spec")
            price = item.find('div', class_="price-to-cart").find('div', class_="sale")

            stock_info=""
            if not item.find('div', class_="sales-price") and not item.find('div', class_="cart-srp"):
                stock_info = "out of stock"

            title_text = ""
            if title is not None:
                title_text = title.strip()

            info_text = ""
            if info is not None:
                info_text = info.text.strip()

            price_text = ""
            if price is not None:
                price_text = price.text.strip()

            output.append(model.computer_info(title_text, info_text, price_text, stock_info))
            

    return output