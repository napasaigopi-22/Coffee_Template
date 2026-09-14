import sqlite3
def search_customer():
    # 1. Connect to a database file (creates 'cafe.db' if it doesn't exist)
    conn = sqlite3.connect("cafe.db")   # it will create or open a database file on my project

    # 2. Create a cursor object to run commands
    cursor = conn.cursor()  # cursor is like an object, it acts like a pointer that executes sql commands.

    # 3. Create a table using SQL syntax
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        total_items INTEGER NOT NULL,
        total_price REAL NOT NULL,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        item_name TEXT NOT NULL,
        item_price REAL NOT NULL,
        FOREIGN KEY(order_id) REFERENCES orders(id)
    )
""")

    # 4. Save (commit) the changes and close the connection

    conn.commit()

    print("Database and 'orders' table created successfully!")

    customer_search = input("enter customer_name:").strip()
    cursor.execute(
        "SELECT * FROM orders WHERE customer_name = ?",(customer_search,)
    )
    customer_orders = cursor.fetchall()

    # --- STAGE 3: DISPLAY RESULTS & CLEANUP ---
    print(f"\n--- Orders for {customer_search} ---")
    if not customer_orders:
        print("No order found!")
    else:
        for order in customer_orders:
            order_id, name, items, price, date = order
            print(
                    f"Order #{order_id} | Name: {name} | Items: {items} | Total: ${price:.2f} | Date: {date}"
                )

        order_search = int(input("enter order_id:"))
        cursor.execute(
            "SELECT item_name, item_price FROM order_items WHERE order_id = ?",(order_search,)
        )
        items_details = cursor.fetchall()
            
        print("Ordered Items:")
        if not items_details:
            print("No order items are there. please try place a NEW Order in coffee_day")
        else:
            for item_name, item_price in items_details:
                print(f"Order details: Item_name:{item_name}, Item_price:{item_price}")
    conn.close()

if __name__ == "__main__":
    search_customer()