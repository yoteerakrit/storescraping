from bs4 import BeautifulSoup
import requests
import csv


# class
class computer_info:
    def __init__(self, title, info, price) -> None:
        self.title = title
        self.info = info
        self.price = price

#function
def computer_info_to_tuple(computer):
    return (computer.title.strip(), computer.info.strip(), computer.price.strip())

def get_request(url):
    res = requests.get(url)
    res.encoding = "utf-8"

    return res
    

def export(file_name, list):
    csv_col = ['title','info','price']

    f_name = "{}.csv".format(file_name)
    f = open(f_name, 'w')

    with f:
        writer = csv.writer(f)

        writer.writerow(csv_col)
        
        for data in list:
            row = computer_info_to_tuple(data)
            print(row)
            writer.writerow(row)



def get_bnn():
    output = []
    page = 1

    page_response = get_request("https://www.bnn.in.th/en/p/desktop-and-all-in-one/desktop?page=1")
    soup_page = BeautifulSoup(page_response.text, 'html.parser')
    
    page_size = soup_page.find('div', class_="product-groups-pagination")['total-page']

    while page != int(page_size) + 1:
        res = get_request("https://www.bnn.in.th/en/p/desktop-and-all-in-one/desktop?page={page}")

        soup = BeautifulSoup(res.text, 'html.parser')
        
        items = soup.find_all('div', class_="product-item-details")

        for item in items:
            title = item.find('div', class_="product-name")
            info = item.find('div', class_="product-short-attribute")
            price = item.find('div', class_="product-price")

            # if item.find_all('div', class_="save-up-to"):

            output.append(computer_info(title.text, info.text, price.text))
            
        page = page + 1

    return output

# call
output = get_bnn()
export("bnn",output)



    



