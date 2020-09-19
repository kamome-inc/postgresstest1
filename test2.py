import psycopg2

def Decorator_open_data_base(func):
    con = psycopg2.connect(
      database="teaching_bd",
      user="pyuser",
      password="admin",
      host="127.0.0.1",
      port="5432"
    )
    func(con)
    con.close()


@Decorator_open_data_base
def main(con):
    cursor = con.cursor()
    cursor.execute('''
            SELECT * FROM schedule
    ''')

    # S.rstrip удаление пробелов справа
    data = cursor.fetchall()[0]


    def data_rstrip(mass):
        # функция для отбрасывания пустых окончаний строк из БД
        print(mass)
        data1 = list()
        for i in range(0, len(mass)):
            if isinstance(mass[i], str):      # проверка совпадения типов данных для строк
                temp = mass[i].rstrip()
            else:
                temp = mass[i]
            data1.append(temp)
        return data1

    print(data_rstrip(data))
