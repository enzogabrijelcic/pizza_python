import mariadb
import sys

class Database:
    def __init__(self, db_name='pizzaria_db', user='root', password='', host='localhost', port=3306):
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=db_name
            )
            self.cursor = self.conn.cursor()
        
        except mariadb.Error as e:
            print(f"Erro de conexão ao MariaDB: {e}")
            sys.exit(1)
     
    def login_user(self, username, password):
        try:
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, password))
            return self.cursor.fetchone()
        except mariadb.Error as e:
            print(f"Erro ao executar login: {e}")
            return None

    def register_user(self, username, password):
        try:
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            self.cursor.execute(query, (username, password))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Erro ao registrar usuário: {e}")

    def get_menu_items(self):
        try:
            query = "SELECT * FROM cardapio"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mariadb.Error as e:
            print(f"Erro ao obter itens do cardápio: {e}")
            return []

    def save_order(self, order_details):
        try:
            query = "INSERT INTO pedido (user_id, items, total_price, payment_method, address, delivery_type) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, order_details)
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Erro ao salvar pedido: {e}")

    def __del__(self):
        if self.conn:
            self.conn.close()
            
    def get_last_order_id(self):
            query = "SELECT LAST_INSERT_ID()"
            self.cursor.execute(query)
            return self.cursor.fetchone()[0]
import mariadb
import sys

class Database:
    def __init__(self, db_name='pizzaria_db', user='root', password='', host='localhost', port=3306):
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=db_name
            )
            self.cursor = self.conn.cursor()
        
        except mariadb.Error as e:
            print(f"Erro de conexão ao MariaDB: {e}")
            sys.exit(1)
     
    def login_user(self, username, password):
        try:
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, password))
            return self.cursor.fetchone()
        except mariadb.Error as e:
            print(f"Erro ao executar login: {e}")
            return None

    def register_user(self, username, password):
        try:
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            self.cursor.execute(query, (username, password))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Erro ao registrar usuário: {e}")

    def get_menu_items(self):
        try:
            query = "SELECT * FROM cardapio"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mariadb.Error as e:
            print(f"Erro ao obter itens do cardápio: {e}")
            return []

    def save_order(self, order_details):
        try:
            query = "INSERT INTO pedido (user_id, items, total_price, payment_method, address, delivery_type) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, order_details)
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Erro ao salvar pedido: {e}")

    def __del__(self):
        if self.conn:
            self.conn.close()
            
    def get_last_order_id(self):
            query = "SELECT LAST_INSERT_ID()"
            self.cursor.execute(query)
            return self.cursor.fetchone()[0]