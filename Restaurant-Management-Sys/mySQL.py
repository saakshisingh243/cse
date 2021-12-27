import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',passwd='root')
mycursor=mycon.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS restaurant")
mycursor.execute("USE restaurant")
mycursor.execute("CREATE TABLE IF NOT EXISTS login(username varchar(25) PRIMARY KEY,password varchar(25) NOT NULL,display_name varchar(70))")
mycursor.execute("CREATE TABLE IF NOT EXISTS fooditems(itemid int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, category varchar(125) NOT NULL, item_name varchar(255) NOT NULL, quantity varchar(50), item_price varchar(15) NOT NULL)")
#mycursor.execute('INSERT INTO login VALUES("admin","admin","The Administrator")')
mycon.commit()
