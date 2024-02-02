import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",password="",charset="utf8",database="pydb")
if con.is_connected():
    print("Successfully Connected to MySQL database")
else:
    print("Failed to Connect to MySQL database")
crsr=con.cursor()
crsr.execute('create table empl(EMPNO int primary key,ENAME varchar(10) unique,JOB varchar(10),MGR int,HIREDATE date,sal float(6,2),comm float(6,2),deptno tinyint)')
