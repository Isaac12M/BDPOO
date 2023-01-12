import psycopg2

try:
    conecction=psycopg2.connect(
        host='localhost',
        port='5432',
        user='postgres',
        password='1234'
    )
    print("conexión_exitosa")
except Exception as ex:
    print(ex)    