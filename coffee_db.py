import sqlite3

DATABASE_NAME = "cafe.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            total_items INTEGER NOT NULL,
            total_price REAL NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            item_name TEXT NOT NULL,
            item_price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id)
        )
        """
    )

    conn.commit()
    conn.close()


def create_order(customer_name, order_items):
    total_items = len(order_items)
    total_price = sum(item["price"] for item in order_items)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO orders (customer_name, total_items, total_price)
        VALUES (?, ?, ?)
        """,
        (customer_name, total_items, total_price),
    )
    order_id = cursor.lastrowid

    for item in order_items:
        cursor.execute(
            """
            INSERT INTO order_items (order_id, item_name, item_price)
            VALUES (?, ?, ?)
            """,
            (order_id, item["name"], item["price"]),
        )

    conn.commit()
    conn.close()
    return order_id


def get_order(order_id):
    conn = get_connection()
    order = conn.execute(
        """
        SELECT id, customer_name, total_items, total_price, order_date
        FROM orders
        WHERE id = ?
        """,
        (order_id,),
    ).fetchone()
    conn.close()
    return order


def get_order_items(order_id):
    conn = get_connection()
    items = conn.execute(
        """
        SELECT item_name, item_price
        FROM order_items
        WHERE order_id = ?
        """,
        (order_id,),
    ).fetchall()
    conn.close()
    return items


def get_all_orders():
    conn = get_connection()
    orders = conn.execute(
        """
        SELECT id, customer_name, total_items, total_price, order_date
        FROM orders
        ORDER BY id DESC
        """
    ).fetchall()
    conn.close()
    return orders


def search_orders_by_customer(customer_name):
    conn = get_connection()
    orders = conn.execute(
        """
        SELECT id, customer_name, total_items, total_price, order_date
        FROM orders
        WHERE customer_name LIKE ?
        ORDER BY id DESC
        """,
        (f"%{customer_name}%",),
    ).fetchall()
    conn.close()
    return orders

def delete_order_detail(order_id):
    conn = get_connection()
    orders = conn.execute(
        """
        DELETE FROM order_items
        WHERE order_id = ? """,
        (order_id,),
    )

    orders.execute(
        """DELETE FROM orders
        WHERE id = ?
        """,
        (order_id,),
    )
    conn.commit()
    conn.close()

def search_customer():
    init_db()
    customer_name = input("Enter customer name: ").strip()
    orders = search_orders_by_customer(customer_name)

    print(f"\n--- Orders for {customer_name} ---")
    if not orders:
        print("No order found.")
        return

    for order in orders:
        print(
            f"Order #{order['id']} | Name: {order['customer_name']} | "
            f"Items: {order['total_items']} | Total: ${order['total_price']:.2f} | "
            f"Date: {order['order_date']}"
        )

    order_id = int(input("Enter order id: "))
    items = get_order_items(order_id)

    if not items:
        print("No order items found.")
        return

    for item in items:
        print(f"Item: {item['item_name']}, Price: ${item['item_price']:.2f}")



if __name__ == "__main__":
    search_customer()
