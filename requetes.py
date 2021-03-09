import mysql.connector

# Connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="student",
  password="mdpSQL2021",
  database='e_commerce'
)
mycursor = mydb.cursor()

# Nombre de clients total
nb_clients = '''
            SELECT COUNT(*) 
            FROM Customers
            '''
mycursor.execute(nb_clients)
myresult = mycursor.fetchall()
print(myresult)

# Nombre de produits total
nb_produits = '''
            SELECT COUNT(product_id)
            FROM Products
            '''
mycursor.execute(nb_produits)
myresult = mycursor.fetchall()
print(myresult)

# Nombre de produits par catégorie
nb_pro_cat = '''
            SELECT product_category_name, COUNT(product_id) 
            FROM Products
            GROUP BY product_category_name
            ORDER BY COUNT(product_id) DESC
            '''
mycursor.execute(nb_pro_cat)
myresult = mycursor.fetchall()
print(myresult)

# Nombre de commandes total
nb_order_total = '''
                SELECT COUNT(DISTINCT order_id)
                FROM Orders
                '''
mycursor.execute(nb_order_total)
myresult = mycursor.fetchall()
print(myresult)

# Nombre de commande selon leurs états (en cours de livraison...)
nb_order_by_status = '''
                    SELECT order_status, COUNT(DISTINCT order_id)
                    FROM Orders
                    GROUP BY order_status
                    '''
mycursor.execute(nb_order_by_status)
myresult = mycursor.fetchall()
print(myresult)

# Nombre de commande par mois
nb_order_by_month = '''
                    SELECT EXTRACT(MONTH FROM order_purchase_timestamp) AS Month, COUNT(DISTINCT order_id)
                    FROM Orders
                    GROUP BY Month
                    '''
mycursor.execute(nb_order_by_month)
myresult = mycursor.fetchall()
print(myresult)

# Prix moyen d'une commande
avg_price = '''
            WITH Total AS
            (
            SELECT DISTINCT(order_id), SUM(payment_value) AS pv 
            FROM Order_payments
            GROUP BY order_id
            )
            SELECT AVG(pv)
            FROM Total
            '''
mycursor.execute(avg_price)
myresult = mycursor.fetchall()
print("prix moyen d'une commande")
print(myresult)

# Score de satisfaction moyen
mean_score_reviews = ''' 
                    SELECT AVG(review_score) 
                    FROM Order_reviews
                    '''
mycursor.execute(mean_score_reviews)
myresult = mycursor.fetchall()
print("score de satisfaction moyen")
print(myresult)

# Nombre de vendeurs
nb_sellers = ''' 
            SELECT COUNT(DISTINCT seller_id) 
            FROM Sellers 
            '''
mycursor.execute(nb_sellers)
myresult = mycursor.fetchall()
print(myresult)

# Nombre de vendeurs par région
nb_sellers_by_state = '''
                    SELECT seller_state, COUNT(DISTINCT seller_id) 
                    FROM Sellers
                    GROUP BY seller_state
                    '''
mycursor.execute(nb_sellers_by_state)
myresult = mycursor.fetchall()
print(myresult)

#-------------
# Requetes partie 2
# Quantité de produit vendu par catégorie

# Nombre de commande par jour
nb_comm_by_day = '''
                SELECT EXTRACT(DAY FROM order_purchase_timestamp) AS Day, COUNT(DISTINCT order_id)
                FROM Orders
                GROUP BY Day
                '''
mycursor.execute(nb_comm_by_day)
myresult = mycursor.fetchall()
print(myresult)

# Nombre de commande par jour de la semaine
nb_comm_by_day_of_week = '''
                SELECT DAYOFWEEK(order_purchase_timestamp) AS Day_of_week, COUNT(DISTINCT order_id)
                FROM Orders
                GROUP BY Day_of_week
                '''
mycursor.execute(nb_comm_by_day_of_week)
myresult = mycursor.fetchall()
print(myresult)

# Durée moyenne entre la commande et la livraison
avg_time = '''
          SELECT AVG(DATEDIFF(order_delivered_customer_date, order_purchase_timestamp))
          FROM Orders
          '''
mycursor.execute(avg_time)
myresult = mycursor.fetchall()
print(myresult)

# Nombre de commande par ville (ville du vendeur)
# nb_comm_by_city = '''
#                   SELECT COUNT(DISTINCT Order_items.order_id), Order_items.seller_id, Sellers.seller_id, Sellers.seller_city AS City
#                   FROM Order_items
#                   INNER JOIN Sellers
#                   ON Order_items.seller_id = Sellers.seller_id
#                   GROUP BY City
#                   '''
# mycursor.execute(nb_comm_by_city)
# myresult = mycursor.fetchall()
# print(myresult)

# Prix minimum des commandes
min_price = '''
            WITH Total AS
            (
            SELECT DISTINCT(order_id), SUM(payment_value) AS pv 
            FROM Order_payments
            GROUP BY order_id
            )
            SELECT MIN(pv)
            FROM Total
            '''
mycursor.execute(min_price)
myresult = mycursor.fetchall()
print(myresult)

# Prix maximum des commandes
max_price = '''
            WITH Total AS
            (
            SELECT DISTINCT(order_id), SUM(payment_value) AS pv 
            FROM Order_payments
            GROUP BY order_id
            )
            SELECT MAX(pv)
            FROM Total
            '''
mycursor.execute(max_price)
myresult = mycursor.fetchall()
print(myresult)

# Temps moyen d'une livraison par mois

# Insertion d'un produit dans Products
# new_product = '''
#               INSERT INTO Products (
#               product_id VARCHAR(50),
#               product_category_name VARCHAR(50),
#               product_name_length FLOAT,
#               product_description_length INT,
#               product_photos_qty INT,
#               product_weight_g INT,
#               product_length_cm INT,
#               product_height_cm INT,
#               product_width_cm INT
#               )
#               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#               '''
# val = (1112, cool_stuff, 5, 250, 1, 50, 22, 21,20)
#
#mycursor.executemany(sql, val)
#mydb.commit()