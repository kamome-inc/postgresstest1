file_name = "schedule_data_1.txt"

file = open(file_name, 'r')

# print(*file)
# print(file.readlines())
i = 0
request = []

for line in file.readlines():
    temp = line.split('\t')
    words = []
    for item in temp:
        if item == 'нечет\n':
            item = 'True'
        elif item == 'чет\n':
            item = 'False'
        words.append(item)
    # print(words)
    # words[1] = int(words[1])

    request.append(words)
# print(request)
file.close()

req = """INSERT INTO public.schedule (day_name, class_time, group_name, classroom, class_type, subject, is_week_odd)
        VALUES """

for line in request:
    req = req + '(' + ','.join(map(lambda word: '\'' + word + '\'', line)) + '),'

req = req[:len(req)-1] + ';'
print(req)