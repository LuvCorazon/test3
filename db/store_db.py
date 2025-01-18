# store_db.py
import sqlite3
from queries_2 import CREATE_TABLE_store, CREATE_TABLE_products_details, INSERT_store_query, \
    INSERT_products_details_query

# Подключение к базе данных
db = sqlite3.connect('db/registered.sqlite3')  # Указываем путь к базе данных
cursor = db.cursor()


# Функция для создания таблиц
async def create_db():
    try:
        # Подключение к базе данных
        if db:
            print('База данных подключена')

        # Выполняем создание таблиц
        cursor.execute(CREATE_TABLE_store)
        cursor.execute(CREATE_TABLE_products_details)

        db.commit()  # Сохраняем изменения
        print("Таблицы успешно созданы.")
    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")


# Функция для вставки данных в таблицу store
async def sql_insert_store(name_product, size, price, photo, productid):
    try:
        cursor.execute(INSERT_store_query, (name_product, size, price, photo, productid))
        db.commit()  # Сохраняем изменения
        print("Данные успешно добавлены в таблицу store.")
    except Exception as e:
        print(f"Ошибка при добавлении данных в таблицу store: {e}")


# Функция для вставки данных в таблицу products_details
async def sql_insert_products_details(productid, category, infoproduct):
    try:
        cursor.execute(INSERT_products_details_query, (productid, category, infoproduct))
        db.commit()  # Сохраняем изменения
        print("Данные успешно добавлены в таблицу products_details.")
    except Exception as e:
        print(f"Ошибка при добавлении данных в таблицу products_details: {e}")
