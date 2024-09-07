
import mysql.connector
#establishing a connection
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="aidsiib"
)

#creating a cursor object using the cursor() method
cursor=mydb.cursor()


#create table

sql=''' select * from subjects'''
#execute the query
cursor.execute(sql)
#fetch the 1st row
result=cursor.fetchone();
print(result)

#fetch all
result=cursor.fetchall();
print(result)
#closing the connection
mydb.close()