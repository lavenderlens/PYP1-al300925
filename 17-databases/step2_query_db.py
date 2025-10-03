import sqlite3
with sqlite3.connect('my_database.db') as conn:
    c = conn.cursor()

    # print all products
    c.execute("SELECT * FROM products")
    all_items = c.fetchall()
    print(type(all_items))#<class 'list'> list OF tuples

    print("All items:")
    for item in all_items:
        print(item)
    print("*" * 50)

    # different queries:
    c.execute("SELECT * FROM products WHERE price > :price", {'price': 3.00})
    price_over_3 = c.fetchall()
    print("Items over £3")
    for item in price_over_3:
        print(item)
    print("*" * 50)

    # these queries are read-only
    # what if we wish to UPDATE items in the db?
    # this will persist changes to permanent storgae
    c.execute("""
            UPDATE products SET price = :price
            WHERE prodId = :prodId
            """,
            {'prodId': '111', 'price':10.50})
    c.execute("""DELETE FROM products
              WHERE description = :description""",
              {'description':"Flat White"})#case sensitive - it must be Python
    
    # print our products table after changes:
    c.execute("SELECT * FROM products")

    edited_items = c.fetchall()
    print("AFTER udating Earl Gret price and removing flat White")
    for item in edited_items:
        print(item)
    print("*" * 50)
