from bs4 import BeautifulSoup
import helper
import model

def get_bnn(url):
    output = []
    page = 1

    page_response = helper.get_request(url.replace("pagesize", str(1)))
    soup_page = BeautifulSoup(page_response.text, 'html.parser')
    
    page_size = soup_page.find('div', class_="product-groups-pagination")['total-page']

    while page != int(page_size) + 1:
        res = helper.get_request(url.replace("pagesize", str(page)))

        soup = BeautifulSoup(res.text, 'html.parser')
        
        items = soup.find_all('div', class_="product-item")
        
        for item in items:
            top = item.find('div', class_="product-item-top")
            stock_info = ""
            if top.find('div', class_="badge-inactive"):
                top_info = top.find('div', class_="badge-inactive")
                data = top_info.find('b')
                stock_info = data.text

            details = item.find('div', class_="product-item-details")

            title = details.find('div', class_="product-name")
            info = details.find('div', class_="product-short-attribute")
            price = details.find('div', class_="product-price")

            info_text = ""
            if info is not None:
                info_text = info.text.strip()

            title_text = ""
            if title is not None:
                title_text = title.text.strip()

            price_text = ""
            if price is not None:
                price_text = price.text.strip()

            output.append(model.computer_info(title_text, info_text, price_text, stock_info))
            
        page = page + 1

    return output
