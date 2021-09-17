import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",passwd="cs",charset="utf8",database="kinshuk")
cur=con.cursor()
cur.execute("DELETE FROM STUDENT WHERE ADMN_NO=1245")
con.commit()
