"""
import datetime

import time
print(time.gmtime())

t = str(datetime.datetime.now())
print(datetime.datetime.now())
"""
import psycopg2

con = psycopg2.connect(
    database="test2",
    user="postgres",
    password="ghjn0nbg",
    host="127.0.0.1",
    port="5432"
)

file_name = "cities 1584.txt"

file = open(file_name, 'r')

# print(*file)
# print(file.readlines())
i = 0
request = []

for line in file.readlines():
    request.append(line[:len(line)-1])
print(request)
print(len(request))
file.close()

req = '''INSERT INTO public.cities(
    name)
    VALUES '''

i = 0
for line in request:
    req = req + '(\'' + line + '\'' + '),'
    i = i + 1
    if line == '':
        print(i, 'ERROR')
req = req[:len(req)-1] + ';'
print(req)
con.close()

