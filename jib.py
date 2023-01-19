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

        print(info.text)

        title_text = ""
        if title is not None:
            title_text = title.strip()

        info_text = ""
        if info is not None:
            info_text = info.text.strip()

        price_text = ""
        if price is not None:
            price_text = price.text.strip()

        output.append(model.computer_info(title_text, info_text, price_text, ""))
    
    return output