import mysql.connector
import time

mydb = mysql.connector.connect(host="localhost",user="root", passwd = 't123456', database = "kursovadb")

mycursor = mydb.cursor(buffered=True)

mycursor.execute("select * from temperature")

def set_data(data):
    sqlform = ('INSERT INTO `temperature`(temperatureoutput) VALUES (%s)')
    mycursor.executemany(sqlform, data)
    mydb.commit()

