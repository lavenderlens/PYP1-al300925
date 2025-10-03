import sqlite3

with sqlite3.connect('my_database.db') as conn:
    print(type(conn))#<class 'sqlite3.Connection'>
    c = conn.cursor()
    print(type(c))#<class 'sqlite3.Cursor'>

    c.execute(
        """
        CREATE TABLE products (
        prodId text,
        description text,
        price float)
        """
    )
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)",
              {'prodId': '111', 'description':'Earl Grey', 'price':1.99})
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)",
              {'prodId': '222', 'description':'Americano', 'price':2.50})
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)",
              {'prodId': '333', 'description':'Capuccino', 'price':3.00})
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)",
              {'prodId': '444', 'description':'Caffe Late', 'price':3.50})
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)",
              {'prodId': '555', 'description':'Flat White', 'price':3.50})
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)",
              {'prodId': '666', 'description':'Hot Chocolate', 'price':3.65})