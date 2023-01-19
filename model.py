class computer_info:
    def __init__(self, title, info, price, stock_info) -> None:
        self.title = title
        self.info = info
        self.price = price
        self.stock_info = stock_info

def computer_info_to_tuple(computer):
    return (computer.title.strip(), computer.info.strip(), computer.price.strip(), computer.stock_info.strip())