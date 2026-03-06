with open('text.txt', 'w') as file:
    lines = ["первая строка",
             "вторая строка",
             "третья строка",
             "четвертая строка",
             "пятая строка"]
    for line in lines:
        file.write(line + '\n')

with open('text.txt', 'r') as file:
    prim = file.readlines()
for i in prim:
    print(i)

num_lines = len(prim)
words_in_file = sum(len(line.split()) for line in prim)
long_str = max(prim, key=len)
print("кол-во строк в файле", num_lines)
print("кол-во слов в файле", words_in_file)
print("саммая длинная строка:", long_str)