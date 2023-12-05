import mysql.connector

conexion = mysql.connector.connect(
    user='root', 
                                    password='miawbtsthebest',
                                    host='localhost',
                                    database='musicvj',
                                    port='3306')

print(conexion)