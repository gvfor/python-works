product={"id":200, "title":"tshirt", "price":300, "brand":"lv"}

print(product["brand"])

# update
product["price"]=500  

# add
product["date"]=10

print(product)



# add offer as 10 if offer exist else add offer as 20

if "offer" in product:
    product["offer"]=10

else:
    product["offer"]=20

    print(product)