import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",passwd="",charset="utf8",database="pydb")
cur=con.cursor()
cur.execute("UPDATE STUDENT SET MARKS=55.68 WHERE ADMN_NO=1245")
con.commit()
