import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",passwd="",charset="utf8",database="pydb")
cur=con.cursor()
cur.execute("SELECT*FROM SOFTDRINK")
for k in cur:
    print(k)
