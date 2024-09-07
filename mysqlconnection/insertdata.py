import mysql.connector

#establishing the connection
mydb=mysql.connector.connect(
	host='localhost',
	user='root',
	password='root',
	database='aidsiib'
)
#creating a cursor object using the cursor() method
cursor=mydb.cursor()

#insert data into subjects table
sql="""insert into subjects(
	name,faculty)
	values('Python Lab','Sana Mam')"""

try:
	#execute the command
	cursor.execute(sql)
	#commit changes
	mydb.commit()
except:
	#rolling back in case of error
	mydb.rollback()

mydb.close()
