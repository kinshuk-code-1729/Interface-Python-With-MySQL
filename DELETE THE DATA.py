import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",passwd="",charset="utf8",database="pydb")
cur=con.cursor()
cur.execute("DELETE FROM STUDENT1 WHERE SID=1245")
con.commit()
