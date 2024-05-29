import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',          #datos bd
    password ='',
    database = 'basedatos_python'
)
