orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]

orders_count={}

for item in orders:

    if item in orders_count:

        orders_count[item]+=1

    else:
        
        orders_count[item]=1

print(orders_count)
    