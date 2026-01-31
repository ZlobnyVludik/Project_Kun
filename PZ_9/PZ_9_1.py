# В магазинах имеются следующие товары.
# Магнит – молоко, соль, сахар.
# Пятерочка – мясо, молоко, сыр.
# Перекресток – молоко, творог, сыр, сахар.
# Определить:
# 1. в каких магазинах нельзя приобрести сыр.
# 2. в каких магазинах можно приобрести одновременно молоко и сахар.
# 3. в каких магазинах можно приобрести соль.

# Множества
magnit = {"Соль", "Молоко", "Сахар"}
pyatka = {"Мясо", "Молоко", "Сыр"}
prkrst = {"Молоко", "Творог", "Сыр", "Сахар"}

# Список
stores_dict = {
    "Магните": magnit,
    "Пятерочке": pyatka,
    "Перекрестке": prkrst
}

# Задание 1
no_cheese = [stores for stores, stock in stores_dict.items() if "Сыр" not in stock]
print("Сыра нет в", no_cheese)

# Задание 2
m_and_s = [stores for stores, stock in stores_dict.items() if {"Молоко", "Сахар"}.issubset(stock)]
print("Молоко и сахар можно купить в", m_and_s)

# Задание 3
salty = [stores for stores, stock in stores_dict.items() if "Соль" in stock]
print("Соль можно купить в", salty)
