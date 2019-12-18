import json
from utils import convert_price_to_number
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Product import CProduct

NUMBER_OF_PAGES_TO_SEARCH = 5
ELEMENTS_ON_PAGE = 64

URL = "https://www.emag.ro/homepage"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome(executable_path=r"C:\\Users\\Babi\\Downloads\\chromedriver\\chromedriver.exe",
                          chrome_options=options)

search_term = str(input("What are you looking for?\n:"))

driver.get(URL)
element = driver.find_element_by_xpath('//*[@id="searchboxTrigger"]')
element.send_keys(search_term)
element.send_keys(Keys.ENTER)

products = []

page = NUMBER_OF_PAGES_TO_SEARCH

while page != 0:
    if page != 0:
        try:
            driver.get(driver.current_url + "&page=" + str(page))
        except:
            break
    for i in driver.find_elements_by_xpath("//*[@id='card_grid']"):
        counter = 0
        for j in range(ELEMENTS_ON_PAGE):
            should_add = True
            name = ""
            price = ""
            prev_price = ""
            link = ""
            try:
                name = i.find_elements_by_tag_name('h2')[counter].text
                price = convert_price_to_number(i.find_elements_by_class_name('product-new-price')[counter].text)
                link = i.find_elements_by_xpath('//h2/a')[counter].get_attribute("href")
                try:
                    prev_price = convert_price_to_number(i.find_elements_by_class_name('product-old-price')[counter]
                                                         .text)
                except:
                    prev_price = price
            except:
                print("exception")
                should_add = False
            product = CProduct(name, price, prev_price, link)
            if should_add:
                products.append(product)
            counter = counter + 1
        page = page - 1
        print(page)


biggest_discount = 0.0
lowest_price = 0.0
cheapest_product = CProduct("", "", "", "")
best_deal_product = CProduct("", "", "", "")
search_terms = search_term.split(" ")

run = 0

for product in products:
    not_right = False
    for word in search_terms:
        if word.lower() not in product.name.lower():
            not_right = True
        if not not_right:
            if run == 0:
                lowest_price = product.price
                cheapest_product = product
                run = 1
            elif product.price < lowest_price:
                lowest_price = product.price
                cheapest_product = product
            discount = product.prev_price - product.price
            if discount > biggest_discount:
                biggest_discount = discount
                best_deal_product = product

with open('products.json', 'w') as json_file:
    data = {}
    data["Products"] = []
    for prod in products:
        data["Products"].append(prod.serialize())
    json.dump(data, json_file, sort_keys=True, indent=4)

print(json.dumps(cheapest_product.serialize(), indent=4, sort_keys=True))
print(json.dumps(best_deal_product.serialize(), indent=4, sort_keys=True))
