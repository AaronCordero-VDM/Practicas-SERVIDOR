#!E:\Python3.11\python.exe

import mysql.connector
import sys
from mysql.connector import Error


#   1. Clase que implementa las operaciones con la base de datos
class BDVideojuegos:
    #   1.1 Constructor del objeto para conectar con la BBDD
    def create_db_connection(host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection
    
    
    def execute_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            cursor.close()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
            
    def read_query(connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as err:
            print(f"Error: '{err}'")
        
        
    #   1.2 Pedimos todos los datos y los devolvemos 
    def todosLosVideojuegos(self):
        select = "SELECT * FROM videojuegosantiguos ORDER BY nombre ASC"
        conection = self.create_db_connection("localhost","root", pw, db)
        results = self.read_query(conection,select)
        #   Traza para ver el objeto mi_resultado en el error log
        sys.stderr.write(str(results))

        #   Cerramos el cursor 

        return results
    
#   En 'principal' hacemos pruebas para ver si funciona (paso 2)

    #   5. Filtrar los videojuegos 
    #------------------------
    # Crearemos una funcion Consulta que le pasare el filtro y si esta vacio, que realice la consulta
    # normal, sino que haga la que contiene el where y asi podemos hacerlo en solo 1 funcion
    #------------------------
    def juegosConFiltro(self, filtro):

        #   Crear el texto de la consulta
        consulta = f"SELECT * FROM videojuegosantiguos {filtro} ORDER BY nombre"
        conection = self.create_db_connection("localhost","root", pw, db)
        results = self.read_query(conection,consulta)
        #   Traza para ver el objeto mi_resultado en el error log
        sys.stderr.write(str(results))

        return results
    