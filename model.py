class computer_info:
    def __init__(self, brand, title, info, price, full_price, discount, stock_info) -> None:
        self.brand = brand
        self.title = title
        self.info = info
        self.price = price
        self.full_price = full_price
        self.discount = discount
        self.stock_info = stock_info

def computer_info_to_tuple(computer):
    return (computer.brand.strip(), computer.title.strip(), computer.info.strip(), computer.price.strip(), computer.full_price.strip(), computer.discount.strip(), computer.stock_info.strip())