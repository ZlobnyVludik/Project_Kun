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

