import psycopg2

con = psycopg2.connect(dbname='test1', user='user1', password='admin', host='localhost')

cursor = con.cursor()

cursor.execute('Select * from users')

print(cursor.fetchall())

cursor.close()
con.close()