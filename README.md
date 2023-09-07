"# supermarket" 
# Online Shopping Web Application


This is a simple web application built with Flask that allows users to sign up, log in, and perform basic shopping activities. Users can view products, add them to a shopping cart, view the cart, and proceed to checkout.

![Demo](demo.gif)

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Features

- **User Registration**: Users can sign up by providing their first name and a unique customer ID.

- **User Login**: Registered users can log in using their first name and customer ID.

- **Product Listing**: Users can view a list of available products with prices and add them to their cart.

- **Shopping Cart**: Users can add products to their shopping cart, view the cart, and see the total price.

- **Checkout**: Users can review their cart contents and confirm their purchase.

## Getting Started

Follow these steps to set up and run the application locally.

1. Clone this repository to your local machine:

   ```shell
   git clone <https://github.com/nadavc25/supermarket.git>

2. Install the required dependencies using pip:
pip install -r requirements.txt
3. Start the Flask application:
python app.py

## Project Structure

The project structure is organized as follows:

- `app.py`: The main application file containing Flask routes and logic.
- `templates/`: Contains HTML templates for different pages.
- `customers.json`: JSON file for storing customer data.
- `requirements.txt`: List of Python dependencies.

## Usage

1. Register a new account by clicking the "Sign Up" link on the home page.

2. Log in with your registered credentials on the "Login" page.

3. Browse available products on the "Customer Menu" page and add them to your cart.

4. View your cart contents and the total price on the "View Cart" page.

5. Proceed to checkout to confirm your purchase.


## Acknowledgments

This project was created as a learning exercise and is not meant for production use. It serves as a starting point for building more complex e-commerce applications.