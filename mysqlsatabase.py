import mysql.connector

class MySQLDatabase:

    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.conn = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        self.conn.close()

    def execute_query(self, query, values=None):
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()

    def insert(self, table_name, data):
        try:
            self.connect()
            cursor = self.conn.cursor()
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            values = tuple(data.values())
            sql = "INSERT INTO {} ({}) VALUES ({})".format(table_name, columns, placeholders)
            cursor.execute(sql, values)
            self.conn.commit()
            print(cursor.rowcount, "record inserted.")
        except Exception as e:
            print("Error while inserting data: ", e)
        finally:
            self.disconnect()

    def search(self, table_name, column_name, value):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = "SELECT * FROM {} WHERE {}=%s".format(table_name, column_name)
            cursor.execute(sql, (value,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("Error while searching data: ", e)
        finally:
            self.disconnect()

    def create_table(self, table_query, table_name):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            if (table_name,) in tables: # Oluşturulmak istenen tablo zaten var ise:
                print(f"The table {table_name} already exists.")
                return True
            cursor.execute(table_query)
            result = cursor.fetchall()
            self.conn.commit()
            return result
        except Exception as e:
            print("Error while creating table: ", e)
        finally:
            self.disconnect()

    def update(self, table, data, where):
        try:
            self.connect()
            cursor = self.conn.cursor()
            if not data or not where:
                return
            set_values = []
            for key, value in data.items():
                set_values.append(f"{key} = '{value}'")
            set_values = ', '.join(set_values)
            conditions = []
            for key, value in where.items():
                conditions.append(f"{key} = '{value}'")
            conditions = ' AND '.join(conditions)
            query = f"UPDATE {table} SET {set_values} WHERE {conditions}"
            cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print("Error while Updating data: ", e)
        finally:
            self.disconnect()

    def delete(self, table_name, column_name, value):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = "DELETE FROM {} WHERE {}=%s".format(table_name, column_name)
            cursor.execute(sql, (value,))
            self.conn.commit()
            print(cursor.rowcount, "record(s) deleted.")
        except Exception as e:
            print("Error while deleting data: ", e)
        finally:
            self.disconnect()