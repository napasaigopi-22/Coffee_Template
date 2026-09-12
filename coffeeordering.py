import sqlite3

def run_coffee_shop():
    menu = {
        1: ("Espresso", 2.50),
        2: ("Americano", 3.00),
        3: ("Cappuccino", 3.75),
        4: ("Latte", 4.00),
        5: ("Mocha", 4.50),
        6: ("Cold Brew", 4.25),
        7: ("Croissant", 2.75),
        8: ("Blueberry Muffin", 3.25),
    }
    
    order = []
    total_price = 0
    
    print("==========================================")
    print("      WELCOME TO THE PYTHON CAFE ☕       ")
    print("==========================================\n")
    
    
    Customer_Name = input("Enter your Name:").strip()  # strip is used for to remove the unnecessary tabs or spaces before or after. 
    print(f'Hello! {Customer_Name}, Here is your Menu.')
    
    
    for item_num, (item_name,price) in menu.items():
        print(f'{item_num} {item_name},{price}')
    
    while True:
        choice = input("Enter your item number:").strip().lower()
        
        if choice == "done":
            break
        
        if not choice.isdigit():
            print("invalid number, please enter valid input")
            continue
        
        item_num = int(choice)
        
        if item_num in menu:
            item_name, price = menu[item_num]
            order.append((item_num,item_name,price))
            total_price += price
            print(f'added {item_name} to your order')
        else:
            print(f'item {item_num} is not in menu. please select from {1} to {len(menu)}')
        
    print("\n--- YOUR RECEIPT ---")
        
    if order:
        for item_num, item_name, price in order:
            print(f"- {item_name}: ${price:.2f}")

        print(f"total no of items you ordered:{len(order)}")
        print(f"total order value:{total_price}")

        # --- ADD THESE LINES TO SAVE TO DATABASE ---
        conn = sqlite3.connect("cafe.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            total_items INTEGER NOT NULL,
            total_price REAL NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        )
        """)

        cursor.execute(
            """
        INSERT INTO orders (customer_name, total_items, total_price)
        VALUES (?, ?, ?)
        """,
            (Customer_Name, len(order), total_price),
        )

        conn.commit()
        conn.close()
        print("[Thanks! Visit Again]")
        
if __name__ == "__main__":
    run_coffee_shop()
