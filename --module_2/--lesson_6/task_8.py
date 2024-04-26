products = ["Чай", "Мед", "Сахар"]
first_pos, second_pos = 0, 2
products[first_pos], products[second_pos] = products[second_pos], products[first_pos]
print(products)