# THIS FILE IS IRRELEVANT NOW THAT WE CREATE TABLES IN THE 'DATA' FILE
# Create database
import mysql.connector

# Creation of e_commerce database
#mydb = mysql.connector.connect(
#  host="localhost",
#  user="student",
#  password="mdpSQL2021"
#)
#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE e_commerce")

# Connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="student",
  password="mdpSQL2021",
  database='e_commerce'
)
mycursor = mydb.cursor()

# Create Table Customers
create_table_customers = '''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id VARCHAR(50) PRIMARY KEY, 
        customer_unique_id VARCHAR(50), 
        customer_zip_code_prefix INT, 
        customer_city VARCHAR(50), 
        customer_state VARCHAR(50) 
    )
'''
mycursor.execute(create_table_customers)

# Create Table Orders
create_table_orders = '''
    CREATE TABLE IF NOT EXISTS Orders(
        order_id VARCHAR(50),
        customer_id VARCHAR(50),
        order_status VARCHAR(50),
        order_purchase_timestamp DATE,
        order_approved_at DATE,
        order_delivered_carrier_date DATE,
        order_delivered_customer_date DATE,
        order_estimated_delivery_date DATE
    )
'''
mycursor.execute(create_table_orders)


# Create Table Order_reviews
create_table_order_reviews = '''
    CREATE TABLE IF NOT EXISTS Order_reviews(
        review_id VARCHAR(50),
        order_id VARCHAR(50),
        review_score SMALLINT,
        review_comment_title VARCHAR(50),
        review_comment_message VARCHAR(100),
        review_creation_date DATE,
        review_answer_timestamp DATE
    )
'''
mycursor.execute(create_table_order_reviews)

# Create Table Order_payments
create_table_order_payments = '''
    CREATE TABLE IF NOT EXISTS Order_payments(
        order_id VARCHAR(50),
        payment_sequential SMALLINT,
        payment_type VARCHAR(50),
        payment_installments SMALLINT,
        payment_value FLOAT
    )
'''
mycursor.execute(create_table_order_payments)

# Create Table Order_items
create_table_order_items = '''
    CREATE TABLE IF NOT EXISTS Order_items (
        order_id VARCHAR(50),
        order_item_id INT,
        product_id VARCHAR(50),
        seller_id VARCHAR(50),
        shipping_limit_date VARCHAR(50),
        price FLOAT,
        freight_value FLOAT 
    )
    '''
mycursor.execute(create_table_order_items)

# Create Table Products
create_table_products = '''
    CREATE TABLE IF NOT EXISTS Products(
        product_id VARCHAR(50),
        product_category_name VARCHAR(50),
        product_name_length FLOAT,
        product_description_length INT,
        product_photos_qty INT,
        product_weight_g INT,
        product_length_cm INT,
        product_height_cm INT,
        product_width_cm INT
    )
'''
mycursor.execute(create_table_products)

# Create Table Sellers
create_table_sellers = '''
    CREATE TABLE IF NOT EXISTS Sellers(
        seller_id VARCHAR(50),
        seller_zip_code_prefix INT,
        seller_city VARCHAR(50),
        seller_state VARCHAR(50)
    )
'''
mycursor.execute(create_table_sellers)

# Create Table Geolocation
create_table_geolocation = '''
    CREATE TABLE IF NOT EXISTS Geolocation (
        geolocation_zip_code_prefix INT,
        geolocation_lat FLOAT,
        geolocation_lng FLOAT,
        geolocation_city VARCHAR(50),
        geolocation_state VARCHAR(50)
    )
'''
mycursor.execute(create_table_geolocation)
