import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",passwd="",charset="utf8",database="pydb")
cur=con.cursor()
cur.execute("INSERT INTO STUDENT1 VALUES(%s, %s, %s, %s, %s, %s)", (1245, 'Arush', 'M', '2003-10-04', 'science', 67.34))
con.commit()
