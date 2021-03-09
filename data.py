import pandas as pd
import mysql.connector
import csv
import sqlalchemy
import pymysql
engine = sqlalchemy.create_engine("mysql+pymysql://student:mdpSQL2021@localhost/e_commerce")

#Connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="student",
  password="mdpSQL2021",
  database='e_commerce'
)
mycursor = mydb.cursor()

# Data to Tables

customers = pd.read_csv("data/olist_customers_dataset.csv")
customers_df = pd.DataFrame(customers, columns= ['customer_id','customer_unique_id','customer_zip_code_prefix', 'customer_city', 'customer_state'])
print(customers_df.shape)
# we get rid of any duplicates on the customer_unique_id column
customers_df.drop_duplicates(subset=['customer_unique_id'], inplace= True)
print(customers_df.shape)
# import the dataframe into sql table
customers_df.to_sql('Customers', engine, if_exists='replace', index= False)

geolocation = pd.read_csv("data/olist_geolocation_dataset.csv")
geolocation_df = pd.DataFrame(geolocation, columns= ['geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng', 'geolocation_city', 'geolocation_state'])
print(geolocation_df.shape)
geolocation_df.drop_duplicates(subset=['geolocation_zip_code_prefix'], inplace= True)
print(geolocation_df.shape)
geolocation_df.to_sql('Geolocation', engine, if_exists='replace', index= False)

order_items = pd.read_csv("data/olist_order_items_dataset.csv")
order_items_df = pd.DataFrame(order_items, columns= ['order_id', 'order_item_id', 'product_id', 'seller_id', 'shipping_limit_date', 'price', 'freight_value'])
print(order_items_df.shape)
order_items_df.to_sql('Order_items', engine, if_exists='replace', index= False)

order_payments = pd.read_csv("data/olist_order_payments_dataset.csv")
payments_df = pd.DataFrame(order_payments, columns= ['order_id','payment_sequential', 'payment_type', 'payment_installments', 'payment_value'])
print(payments_df.shape)
payments_df.to_sql('Order_payments', engine, if_exists='replace', index= False)

order_reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")
reviews_df = pd.DataFrame(order_reviews, columns= ['review_id','order_id', 'review_score', 'review_comment_title','review_comment_message', 'review_creation_date', 'review_answer_timestamp'])
print(reviews_df.shape)
reviews_df.to_sql('Order_reviews', engine, if_exists='replace', index= False)
#print(reviews_df.describe())

orders = pd.read_csv("data/olist_orders_dataset.csv")
orders_df = pd.DataFrame(orders, columns= ['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date'])
print(orders_df.shape)
orders_df.drop_duplicates(subset=['order_id'], inplace= True)
print(orders_df.shape)
orders_df.to_sql('Orders', engine, if_exists='replace', index= False)

products = pd.read_csv("data/olist_products_dataset.csv")
products_df = pd.DataFrame(products, columns= ['product_id', 'product_category_name', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm'])
print(products_df.shape)
products_df.drop_duplicates(subset=['product_id'], inplace= True)
print(products_df.shape)
products_df.to_sql('Products', engine, if_exists='replace', index= False)

sellers = pd.read_csv("data/olist_sellers_dataset.csv")
sellers_df = pd.DataFrame(sellers, columns= ['seller_id', 'seller_zip_code_prefix', 'seller_city', 'seller_state'])
print(sellers_df.shape)
sellers_df.drop_duplicates(subset=['seller_id'], inplace= True)
print(sellers_df.shape)
sellers_df.to_sql('Sellers', engine, if_exists='replace', index= False)