# Приложение ЗАКАЗЫ ТОВАРОВ для автоматизированного контроля заказов
# торговой фирмы. Таблица Заказы должна содержать информацию о товарах со следующей
# структурой записи: Код товара, Наименование товара, Заказчик (наименование
# организации, возможны повторяющиеся значения), Дата заказа, Срок исполнения (от 1 до
# 10 дней), Стоимость заказа.

import sqlite3 as sq

with sq.connect("orders.db") as con:
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        itm_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        customer TEXT NOT NULL,
        ord_date TEXT NOT NULL,
        deadline INTEGER NOT NULL CHECK(deadline BETWEEN 1 AND 10),
        price INTEGER NOT NULL
    )
    """)

    database = [
        (1, "Товар1", "ООО Арбуз", "10-06-2026", 1, 900),
        (2, "Товар2", "ОАО Шпинат", "11-06-2026", 4, 1200),
        (3, "Товар3", "ООО Помидор", "12-06-2026", 8, 5600),
        (4, "Товар4", "ОАО Шпинат", "12-06-2026", 8, 3333),
        (5, "Товар5", "ООО Арбуз", "13-06-2026", 10, 9990),
        (6, "Товар6", "ООО Жук", "14-06-2026", 6, 5200),
        (7, "Товар7", "ООО Жук", "15-06-2026", 5, 1677),
        (8, "Товар8", "ОАО Фаренгейт", "16-06-2026", 6, 1313),
        (9, "Товар9", "ОАО Шпинат", "16-06-2026", 7, 44444),
        (10, "Товар10", "ООО Мартышка", "16-06-2026", 2, 900)
    ]

    cur.execute("DELETE FROM orders")
    cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)", database)

    print("База данных:")
    cur.execute("SELECT * FROM orders")
    for result in cur:
        print(result)

    # На поиск
    print("\nПоиск 1")
    cur.execute("SELECT * FROM orders WHERE customer = 'ОАО Шпинат'")
    for result in cur:
        print(result)

    print("\nПоиск 2")
    cur.execute("SELECT * FROM orders WHERE price BETWEEN 2000 AND 8000")
    for result in cur:
        print(result)

    print("\nПоиск 3")
    cur.execute("SELECT * FROM orders WHERE deadline <= 5")
    for result in cur:
        print(result)

    # На редактирование
    cur.execute("UPDATE orders SET price = 1000 WHERE itm_id = 1")
    cur.execute("UPDATE orders SET deadline = 5 WHERE customer = 'ОАО Шпинат' AND price = 44444")
    cur.execute("UPDATE orders SET price = 1500, deadline = 7 WHERE customer LIKE '%Ф%'")

    print("\nПосле редактирования:")
    cur.execute("SELECT * FROM orders")
    for result in cur:
        print(result)

    # На удаление
    cur.execute("DELETE FROM orders WHERE itm_id = 10")
    cur.execute("DELETE FROM orders WHERE customer = 'ОАО Шпинат'")
    cur.execute("DELETE FROM orders WHERE deadline <= 2")

    print("\nПосле удаления:")
    cur.execute("SELECT * FROM orders")
    for result in cur:
        print(result)
