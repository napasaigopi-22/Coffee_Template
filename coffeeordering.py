MENU = {
    1: {
        "name": "Espresso",
        "price": 2.50,
        "description": "A short, bold classic with a clean finish.",
    },
    2: {
        "name": "Americano",
        "price": 3.00,
        "description": "Espresso softened with hot water.",
    },
    3: {
        "name": "Cappuccino",
        "price": 3.75,
        "description": "Espresso, steamed milk, and a soft foam cap.",
    },
    4: {
        "name": "Latte",
        "price": 4.00,
        "description": "Smooth espresso with plenty of steamed milk.",
    },
    5: {
        "name": "Mocha",
        "price": 4.50,
        "description": "Coffee and chocolate blended into a rich cup.",
    },
    6: {
        "name": "Cold Brew",
        "price": 4.25,
        "description": "Slow-steeped coffee served chilled.",
    },
    7: {
        "name": "Croissant",
        "price": 2.75,
        "description": "Flaky, buttery pastry for a quick bite.",
    },
    8: {
        "name": "Blueberry Muffin",
        "price": 3.25,
        "description": "Soft muffin with bright blueberry flavor.",
    },
    9: {
        "name": "Filter Coffee",
        "price": 2.21,
        "description": "Comforting brewed coffee with a familiar taste.",
    },
}


def get_menu_items():
    return [
        {"id": item_id, **item}
        for item_id, item in MENU.items()
    ]


def build_order(selected_item_ids):
    order_items = []

    for item_id in selected_item_ids:
        if item_id in MENU:
            item_name = MENU[item_id]["name"]
            item_price = MENU[item_id]["price"]
            order_items.append(
                {
                    "id": item_id,
                    "name": item_name,
                    "price": item_price,
                }
            )

    total_price = sum(item["price"] for item in order_items)
    return order_items, total_price


def run_coffee_shop():
    from coffee_db import create_order, init_db

    init_db()
    order = []

    print("==========================================")
    print("      WELCOME TO THE PYTHON CAFE")
    print("==========================================\n")

    customer_name = input("Enter your Name: ").strip()
    print(f"Hello! {customer_name}, here is your menu.")

    for item_num, item in MENU.items():
        print(f"{item_num}. {item['name']}: ${item['price']:.2f}")

    while True:
        choice = input("Enter your item number, or done: ").strip().lower()

        if choice == "done":
            break

        if not choice.isdigit():
            print("Invalid number, please enter valid input.")
            continue

        item_num = int(choice)

        if item_num in MENU:
            order.append(item_num)
            print(f"Added {MENU[item_num]['name']} to your order.")
        else:
            print(f"Item {item_num} is not in menu. Please select from 1 to {len(MENU)}.")

    order_items, total_price = build_order(order)

    print("\n--- YOUR RECEIPT ---")
    if not order_items:
        print("No items ordered.")
        return

    for item in order_items:
        print(f"- {item['name']}: ${item['price']:.2f}")

    order_id = create_order(customer_name, order_items)
    print(f"Total items: {len(order_items)}")
    print(f"Total order value: ${total_price:.2f}")
    print(f"Order ID: {order_id}")
    print(f"Thanks! Visit again {customer_name}.")


if __name__ == "__main__":
    run_coffee_shop()
