import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",passwd="kb",charset="utf8",database="MYSQL")
cur=con.cursor()
cur.execute("SELECT*FROM HELP_TOPIC")
for k in cur:
    print(k)
