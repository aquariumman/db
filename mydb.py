import pymysql
from decorator import decor_for_connect

#Open database connection
try:
    db = pymysql.connect(
        host='127.0.0.1',
        user='imalo',
        password='123',
        database='testdb'
    )

except:
    print("Error while connecting to MySQL")

#prepeare a cursor object using cursor() method

cursor = db.cursor()

#Drop table if it already esists using execute() method
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

#Create table as per requrment
sql = """CREATE TABLE EMPLOYEE(
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,
   SEX VARCHAR(2),
   INCOME FLOAT )"""
cursor.execute(sql)

sql = "INSERT INTO EMPLOYEE(FIRST_NAME,\
    LAST_NAME, AGE, SEX, INCOME)\
    VALUES('%s', '%s', '%d', '%c', '%d')" % ('Mac', 'Mohan', 20, 'M', 2000)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

#disconnect from server
print('connection closed!!!')
db.close()