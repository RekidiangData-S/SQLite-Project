import sqlite3
# connect database
conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor() #create a cursor


# Query database order by 

#c.execute("SELECT rowid, * FROM customers ORDER BY rowid ASC")
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
#c.execute("SELECT rowid, * FROM customers ORDER BY name")
c.execute("SELECT rowid, * FROM customers ORDER BY name DESC")




#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

for i in c.fetchall():
	print(i)

# commit our command
conn.commit()
#close connection
conn.close()