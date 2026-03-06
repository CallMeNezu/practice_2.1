with open('students.txt' , 'w') as file:
    students = [{"Иванов Иван" : [5,4,3,5]},
                {"Петров Петр" : [4,3,4,4]},
                {"Сидорова Мария" : [5,5,5,5]}]
    for i in students:
        for key, value in i.items():
            file.write("{} : {}\n".format(key, value))

average_score_students = []
for i in students:
    for key, value in i.items():
        average_score_students.append({key: sum(value) / len(value)})

with open('result.txt' , 'w') as file:
    for i in average_score_students:
        for key, value in i.items():
            if value >= 4:
                file.write("{} : {}\n".format(key, value))

#вывод студентов и их оценок а потом
#студентов со средней оценкой 4+
with open('students.txt', 'r') as file:
    outp_students = file.read()
print(outp_students)

with open('result.txt' , 'r') as file:
    outp_result = file.read()
print(outp_result)