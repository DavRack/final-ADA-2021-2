def order_products(products, atributes):
    atributesOptions = 1
    atributesNames = []
    for atrr in atributes: # a1*a2*...*an
        atributesNames.append(atrr['name'])
        value = ["" for _ in range(len(atrr['value']))]
        for v in atrr['value']:
            index = atrr['value'][v]
            value[index] = v

        atrr['value'] = value
        atributesOptions *= len(atrr['value'])

    # a1*a2*...*an
    allPosibleCombinations = [[0 for _ in atributes] for _ in range(atributesOptions)]

    travel = atributesOptions
    for i,atrr in enumerate(atributes): #a(a1*a2*...*an)
        index = 0
        travel = travel//len(atrr['value'])

        # fills each position of the allPosibleCombinations aray with
        # the combination of atributes
        for _ in range(int(atributesOptions/(len(atrr['value'])*travel))):
            for value in atrr['value']:
                for _ in range(travel):
                    allPosibleCombinations[index][i] = value
                    index += 1

    ordered_products = []

    for combination in allPosibleCombinations: # a1*a2*...*an
        for product in products: # p
            productAtributes = []
            for name in atributesNames: #a
                productAtributes.append(product['atrr'][name])
            if combination == productAtributes:
                ordered_products.append(product)
                break

    return ordered_products

# O(a,p) = ap(a1*a2*a3...)
