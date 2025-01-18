# queries_2.py

CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_product TEXT NOT NULL,
        size TEXT NOT NULL,
        price REAL NOT NULL,
        photo TEXT NOT NULL,
        productid TEXT NOT NULL
    )
"""

CREATE_TABLE_products_details = """
    CREATE TABLE IF NOT EXISTS products_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        productid TEXT NOT NULL,
        category TEXT NOT NULL,
        infoproduct TEXT NOT NULL
    )
"""

INSERT_store_query = """
    INSERT INTO store (name_product, size, price, photo, productid)
    VALUES (?, ?, ?, ?, ?)
"""

INSERT_products_details_query = """
    INSERT INTO products_details (productid, category, infoproduct)
    VALUES (?, ?, ?)
"""
