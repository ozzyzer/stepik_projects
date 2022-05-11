import random

def is_valid(user_number, border):
    if user_number.isdigit() and 1 <= int(user_number) <= border:
        return True
    else:
        return False

print("Добро пожаловать в игру Числовая угадайка!\nВам нужно угадать загаданное программой число от 1 до n")
start_check = "да"
while start_check.lower() == "да":
    border = int(input("Введите верхнюю границу: "))
    number = random.randint(1, border)
    print("Число загадано! Попробуйте угадать!")

    counter = 1
    while True:
        user_number = input("Ваше число: ")
        if is_valid(user_number, border):
            if int(user_number) == number:
                print("Вы угадали! \nЧисло:", number, "\nПопыток использовано:", counter)
                start_check = input("Сыграем еще? Введите \"да\" или \"нет\": ")
                while start_check.lower() not in ["да", "нет"]:
                    print("Введите \"да\" или \"нет\":")
                    start_check = input("Сыграем еще? Введите \"да\" или \"нет\": ")
                break
            elif int(user_number) > number:
                print("Ваше число больше загаданного, попробуйте еще разок")
                counter += 1
            elif int(user_number) < number:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                counter += 1
        else:
            print("Это должно быть целое число от 1 до", border)
else:
    print("До новых встреч!")