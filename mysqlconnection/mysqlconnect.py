
import mysql.connector
#establishing a connection
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="aidsiib"
)
print(mydb)
#creating a cursor object using the cursor() method
cursor=mydb.cursor()

#Dropping subjects table if already exists.
cursor.execute("DROP TABLE IF EXISTS subjects")
#create table

sql=''' create table subjects(
	name char(20) not null,
	faculty char(20) not null
	)'''

cursor.execute(sql)
#closing the connection
mydb.close()