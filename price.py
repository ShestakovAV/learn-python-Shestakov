def format_price(price):
    in_def_price = int(price)
    return f'Цена: {in_def_price} руб.'
price = format_price(56.77)
print(price)