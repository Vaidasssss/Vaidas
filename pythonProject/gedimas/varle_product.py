# # NEBAIKTAS KODAS!!!!!!!!---------------------------------------------------------
#
# # import requests
# # from bs4 import BeautifulSoup
# # import psycopg2
# #
# #
# # def create_and_insert_product():
# #     connection = psycopg2.connect(
# #         host="localhost",
# #         port=5432,
# #         database="products",
# #         user="postgres",
# #         password="302583533"
# #     )
# #
# #     #creating managment wyhith database
# #     cursor = connection.cursor()
# #
# #     create_table_query = """
# #     CREATE TABLE IF NOT EXISTS varle_products(
# #     id SERIAL PRIMARY KEY,
# #     name VARCHAR(255),
# #     price DECIMAL(10, 2),
# #     quantity INT
# #     )
# # """
# #     #execute SQL statemnt
# #     cursor.execute(create_table_query)
# #     print("Table created successfuly")
# #
# #     #define website
# #     url="https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/"
# #
# #     #response from the website
# #     response = requests.get(url)
# #     print(response.content)
# #     soup = BeautifulSoup(response.content,'html.parser')
# #
# #     product_elements = soup.find_all('div', class_= 'ajax-content')
# #
# #     #find all product elements in the category
# #     product_elements = soup.fin_all('div', class_='ajax-container')
# #
# #     #iterate over each product element and extract product information
# #     for product_elements in product_elements:
# #         product_name = product_elements.find('div', class_='product-title').text.strip()
# #         product_price = product_elements.find('span', class_='price-value').text.strip()[:3]
# #         product_quantity = product_element.find('li', class_='stock').text.strip()[:1]
# #
# #         print(product_name)
# #
# #         # insert_query = "INSERT INTO varle_products" (name, price, quantity) VALUE (%s, %s, %s)
# #         # cursor.execute(insert_query, (product_name, product_price, product_quantity))
# #         print(product_name)
# #     connection.commit()
# #     cursor.close()
# #     connection.close()
# #
# #
# #     # connection.commit()
# #     # cursor.close()
# #     # connection.close()
# #
# # if __name__ == '__main__':
# #     create_and_insert_product()
#
# import requests
# from bs4 import BeautifulSoup
# import psycopg2
#
#
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="products",
#         user="postgres",
#         password="302583533"
#     )
#
#     # creating management with database
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS varle_products (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(1000),
#         price DECIMAL(10, 2),
#         quantity INT
#         )
#     """
#
#     # execute SQL statement
#     # cursor.execute(create_table_query)
#     # print("Table created successfully!")


