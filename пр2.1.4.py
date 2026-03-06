from datetime import datetime
from collections import deque

def calculator_def():
    while True:
        try:
            num1 = float(input("введите первое число: "))
            num2 = float(input("введите второе число: "))
            break
        except ValueError:
            print("я сказал числа...")

    deist = input("введите действие(+,-,*,/): ")

    if deist == '+':
        return f"{num1} + {num2} = {num1 + num2}"
    elif deist == '-':
        return f"{num1} - {num2} = {num1 - num2}"
    elif deist == '*':
        return f"{num1} * {num2} = {num1 * num2}"
    elif deist == '/':
        if num2 != 0:
            return f"{num1} / {num2} = {num1 / num2}"
        else:
            return "на ноль делить нельзя"
    else:
        return "такого действия нету"

while True:
    print('''введите:
    1 - ввести пример
    2 - показать последние 5 записей
    3 - очистить весь файл
    0 - выйти''')
    answer_challenge = input(":")
    if answer_challenge == '1':
        calculator_result = calculator_def()
        with open('calculator.log', 'a') as log_file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f"[{timestamp}] {calculator_result}"
            log_file.write(message)
        print(calculator_result)
    elif answer_challenge == '2':
        with open('calculator.log', 'r') as log_file:
            last_line = deque(log_file, maxlen=5)
            for i in last_line:
                print(i.strip())
    elif answer_challenge == '3':
        with open('calculator.log', 'w') as log_file:
            pass
        print("файл очищен")
    elif answer_challenge == '0':
        break
    else:
        print("такого действия нет")