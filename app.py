from flask import Flask, flash, redirect, render_template, request, url_for

from coffee_db import (
    create_order,
    get_all_orders,
    get_order,
    get_order_items,
    init_db,
    search_orders_by_customer,
)
from coffeeordering import build_order, get_menu_items

app = Flask(__name__)
app.secret_key = "python-cafe-development-key"


@app.route("/")
def index():
    return render_template(
        "index.html",
        menu_items=get_menu_items(),
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/order", methods=["POST"])
def order():
    customer_name = request.form.get("customer_name", "").strip()
    selected_items = request.form.getlist("items")

    if not customer_name:
        flash("Please enter your name.")
        return redirect(url_for("index"))

    if not selected_items:
        flash("Please select at least one item.")
        return redirect(url_for("index"))

    selected_item_ids = [int(item_id) for item_id in selected_items]
    order_items, _ = build_order(selected_item_ids)

    if not order_items:
        flash("Please select valid menu items.")
        return redirect(url_for("index"))

    order_id = create_order(customer_name, order_items)
    return redirect(url_for("receipt", order_id=order_id))


@app.route("/receipt/<int:order_id>")
def receipt(order_id):
    order_details = get_order(order_id)
    items = get_order_items(order_id)

    if order_details is None:
        flash("Order not found.")
        return redirect(url_for("orders"))

    return render_template("receipt.html", order=order_details, items=items)


@app.route("/orders")
def orders():
    customer_name = request.args.get("customer_name", "").strip()

    if customer_name:
        order_list = search_orders_by_customer(customer_name)
    else:
        order_list = get_all_orders()

    return render_template(
        "orders.html",
        orders=order_list,
        customer_name=customer_name,
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
