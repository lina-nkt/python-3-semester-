import random

products = ['рыба', 'мясо', 'сталь', 'игрушки', 'одежда', 'книги', 'электроника', 'мебель', 'продукты', 'косметика', 'автомобили', 'инструменты', 'бытовая техника', 'часы', 'обувь']

num_products_factory1 = random.randint(5, 15)
num_products_factory2 = random.randint(5, 15)

factory1 = set(random.sample(products, num_products_factory1))
factory2 = set(random.sample(products, num_products_factory2))

unique_products = factory1.symmetric_difference(factory2)


print("Товары, не повторяющиеся на обоих заводах:")
for product in unique_products:
    print(product)