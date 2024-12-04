cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]

# print count of vehicles
print(f"total vehicles=>{len(cars)}")

# print available colors of baleno
avail_colors=[c.get("colors") for c in cars if c.get("name")=="baleno"]
print(avail_colors[0])

# print all brands
all_brands=[c.get("brand") for c in cars]
print(set(all_brands))

# print car names available in amt transmission
amt_transmission=[c.get("name") for c in cars if c.get("transmission")=="amt"]
print(amt_transmission)