def order_products(products, atributes):
    products_with_weight = []

    for product in products: # O(n,a) = p*2a
        atribute_index = []
        for atrr in atributes:
            atribute_name = atrr["name"]

            categories_count_atrr = len(atrr['value'])
            atrr_position = atrr['value'][product['atrr'][atribute_name]]

            atribute_index.append((categories_count_atrr, atrr_position))

        index = 0
        variable = 1
        for p in range(len(atribute_index)-1,-1,-1):
            atrr = atribute_index[p]
            index += atrr[1]*variable
            variable *= atrr[0]

        products_with_weight.append((index, product))

    ordered_products = sorted(products_with_weight, key=lambda x: x[0]) # O(p) = p*log(p)
    return ordered_products

