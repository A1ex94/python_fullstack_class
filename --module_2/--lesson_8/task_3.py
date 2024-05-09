assortment = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
max_price = max(assortment, key = assortment.get)
min_price = min(assortment, key = assortment.get)
print(f"Самый дешевый: {min_price} - {assortment[min_price]} руб.")
print(f"Самый дорогой: {max_price} - {assortment[max_price]} руб.")