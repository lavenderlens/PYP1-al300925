import sqlite3
with sqlite3.connect('my_database.db') as conn:
    c = conn.cursor()

    c.execute("SELECT * FROM products")
    all_items = c.fetchall()

    print("All items:")
    for item in all_items:
        print(item)
    print("*" * 50)

    # rolling back updates
    c.execute("""UPDATE products SET price = :price
              WHERE prodId = :prodId
              """,
              {'prodId': '111', 'price':1.99})
    c.execute("""INSERT into products VALUES
              (:prodId, :description, :price)""",
              {'prodId': '555', 'description': 'Flat White', 'price':3.50})
    
    c.execute("SELECT * FROM products")

    edited_items = c.fetchall()
    print("AFTER rolling back Earl Grey price and restoring Flat White")
    for item in edited_items:
        print(item)
    print("*" * 50)