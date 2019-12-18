def convert_price_to_number(my_price):
    my_price = my_price.split("Lei")[0]
    my_price = my_price.split(".")[0] + my_price.split(".")[1]
    size = len(my_price)
    my_price = my_price[:size-3] + "." + my_price[size-3:]
    return float(my_price)
