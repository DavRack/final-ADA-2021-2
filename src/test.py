import slow, fast
import time
import copy


import  test500

cases = [10, 20, 50, 100, 200, 300, 400, 500, 1000]
resoults = []

def get_ms():
    return round(time.time() * 1000)
for case in cases:

    atributes = test500.atributes
    products =  test500.products[:case]

    time_fast1 = get_ms()
    ordered_products_fast = fast.order_products(copy.deepcopy(products), copy.deepcopy(atributes))
    ordered_products_fast = fast.order_products(copy.deepcopy(products), copy.deepcopy(atributes))
    ordered_products_fast = fast.order_products(copy.deepcopy(products), copy.deepcopy(atributes))
    ordered_products_fast = fast.order_products(copy.deepcopy(products), copy.deepcopy(atributes))
    ordered_products_fast = fast.order_products(copy.deepcopy(products), copy.deepcopy(atributes))
    time_fast2 = get_ms()

    time_slow1 = get_ms()
    ordered_products_slow = slow.order_products(copy.deepcopy(products), copy.deepcopy(atributes))
    ordered_products_slow = slow.order_products(copy.deepcopy(products), copy.deepcopy(atributes))
    ordered_products_slow = slow.order_products(copy.deepcopy(products), copy.deepcopy(atributes))
    ordered_products_slow = slow.order_products(copy.deepcopy(products), copy.deepcopy(atributes))
    ordered_products_slow = slow.order_products(copy.deepcopy(products), copy.deepcopy(atributes))
    time_slow2 = get_ms()

    resoults.append({"case numbers":case, "slow":(time_slow2-time_slow1)/5,"fast":(time_fast2-time_fast1)/5})

for r in resoults:
    print(r)
