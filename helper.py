import requests
import csv
import model

def get_brand(text):
    # ASUS ACER DELL HP MSI LENOVO ALIENWARE
    lowText = text.lower()
    if "asus" in lowText:
        return "ASUS"
    elif "acer" in lowText:
        return "ACER"
    elif "dell" in lowText:
       return "DELL"
    elif "hp" in lowText:
       return "HP"
    elif "msi" in lowText:
       return "MSI"
    elif "lenovo" in lowText:
        return "LENOVO"
    elif "alienware" in lowText:
        return "ALIENWARE"
    else:
        return ""


def get_request(url):
    res = requests.get(url)
    if res.status_code != 200:
        print(res.status_code)
        return
    
    res.encoding = "utf-8"

    return res   

def get_request_jib(url):
    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

    res = requests.get(url, headers={'User-Agent': userAgent})
    if res.status_code != 200:
        print(res.status_code)
        return
    
    res.encoding = "utf-8"

    return res   

def export(file_name, list, col):
    f_name = "{}.csv".format(file_name)
    f = open(f_name, 'w', encoding="utf-8")

    with f:
        writer = csv.writer(f)

        writer.writerow(col)
        
        for data in list:
            row = model.computer_info_to_tuple(data)
            print(row)
            writer.writerow(row)