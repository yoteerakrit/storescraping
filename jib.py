from bs4 import BeautifulSoup
import helper
import model

def get_jib(category):
    output = []

    res = helper.get_request_jib("https://www.jib.co.th/web/product/product_list/2/category".replace("category", str(category)))

    print(res)

    soup = BeautifulSoup(res.text, 'html.parser')
    
    items = soup.find_all('div', class_="divboxpro")

    print(items)
    
    for item in items:

        details = item.find('div', class_="reladiv")

        title = details.find('div', class_="col-md-12").find('a')['title']
        info = details.find('div', class_="description")
        price = details.find('p', class_="price_total")

        full_price_text = ""
        if details.find('span', class_="price"):
            full_price_text = details.find('span', class_="price").text.replace('-','').replace(',','').strip()

        print(info.text)

        brand_text = ""
        title_text = ""
        if title is not None:
            title_text = title.strip()
            brand_text = helper.get_brand(title_text)

        info_text = ""
        if info is not None:
            info_text = info.text.strip()

        price_text = ""
        if price is not None:
            price_text = price.text.replace('-','').replace(',','').strip()

        output.append(model.computer_info(brand_text, title_text, info_text, price_text, full_price_text, "", ""))
    
    return output