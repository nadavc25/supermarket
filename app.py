from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

try:
    with open('customers.json', 'r') as file:
        customers_lst = json.load(file)
except FileNotFoundError:
    customers_lst = []

products = [
    {"name": "Banana", "price": 1.0, "stock_Inventory": 50},
    {"name": "Carrot", "price": 0.5, "stock_Inventory": 100},
    {"name": "Milk", "price": 2.0, "stock_Inventory": 30},
    {"name": "Meat", "price": 5.0, "stock_Inventory": 20},
    {"name": "Bread", "price": 2.5, "stock_Inventory": 40},
]

def save_customer_data():
    with open('customers.json', 'w') as file:
        json.dump(customers_lst, file)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get user input from the registration form
        first_name = request.form['first_name']
        customer_id = request.form['customer_id']

        # Check if a customer with the provided ID already exists
        existing_customer = next((c for c in customers_lst if c['id'] == customer_id), None)

        if existing_customer:
            return render_template('signup.html', error='Customer ID already exists.')

        # Create a new customer and add them to the customers_lst
        new_customer = {"first_name": first_name, "id": customer_id, "cart": []}
        customers_lst.append(new_customer)
        save_customer_data()
        return redirect(url_for('login'))

    return render_template('signup.html', error=None)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        first_name = request.form['first_name']
        customer_id = request.form['customer_id']

        # Check if a customer with the provided name and ID exists
        customer = next((c for c in customers_lst if c['first_name'] == first_name and c['id'] == customer_id), None)
        
        if customer:
            return redirect(url_for('customer_menu', customer_id=customer_id))
        else:
            return render_template('login.html', error='Customer not found.')

    return render_template('login.html', error=None)

@app.route('/customer_menu/<customer_id>')
def customer_menu(customer_id):
    customer = next((c for c in customers_lst if c['id'] == customer_id), None)
    if customer:
        enumerated_products = list(enumerate(products, start=1))  # Enumerate the products
        return render_template('customer_menu.html', customer=customer, enumerated_products=enumerated_products)
    else:
        return redirect(url_for('login'))
        
@app.route('/add_to_cart/<customer_id>', methods=['POST'])
def add_to_cart(customer_id):
    customer = next((c for c in customers_lst if c['id'] == customer_id), None)
    if customer:
        product_id = int(request.form['product_id'])
        quantity = int(request.form['quantity'])
        product = products[product_id]
        customer['cart'].append({"product": product, "quantity": quantity})
        save_customer_data()
        return redirect(url_for('customer_menu', customer_id=customer_id))
    else:
        return redirect(url_for('login'))

@app.route('/view_cart/<customer_id>')
def view_cart(customer_id):
    customer = next((c for c in customers_lst if c['id'] == customer_id), None)

    if customer:
        cart_contents = []
        total_price = 0

        for item in customer['cart']:
            product = item['product']
            quantity = item['quantity']
            # Check if the product is already in cart_contents
            existing_item = next((ci for ci in cart_contents if ci['product'] == product), None)

            if existing_item:
                # Increment quantity if the product already exists in the cart_contents
                existing_item['quantity'] += quantity
            else:
                # Add the product as a new entry in cart_contents
                cart_contents.append({"product": product, "quantity": quantity})

            # Update the total price
            total_price += product['price'] * quantity

        return render_template('view_cart.html', cart_contents=cart_contents, total_price=total_price, customer=customer)
    else:
        return redirect(url_for('login'))


@app.route('/checkout/<customer_id>', methods=['GET', 'POST'])
def checkout(customer_id):
    customer = next((c for c in customers_lst if c['id'] == customer_id), None)

    if customer:
        if request.method == 'POST':
            # Implement the logic for processing the checkout (e.g., updating stock, clearing the cart, etc.)
            # For now, let's assume the cart is cleared when checking out.
            customer['cart'] = []
            return render_template('customer_menu.html', customer=customer)

        cart_contents = []
        total_price = 0

        for item in customer['cart']:
            product = item['product']
            quantity = item['quantity']
            # Check if the product is already in cart_contents
            existing_item = next((ci for ci in cart_contents if ci['product'] == product), None)

            if existing_item:
                # Increment quantity if the product already exists in the cart_contents
                existing_item['quantity'] += quantity
            else:
                # Add the product as a new entry in cart_contents
                cart_contents.append({"product": product, "quantity": quantity})

            # Update the total price
            total_price += product['price'] * quantity

        return render_template('checkout.html', cart_contents=cart_contents, customer=customer, total_price=total_price)
    else:
        return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True)
