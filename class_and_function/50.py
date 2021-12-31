# python to connect MySQl with Python.
import pymysql

mydb =  pymysql.connect(host="20.204.146.108",user="root",passwd="Expo@123",database="dcb",port = 3306)
cursor = mydb.cursor()
print(mydb)