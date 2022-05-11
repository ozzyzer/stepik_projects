def encrypting(upper_str, lower_str, step):
    caesar_str = ""
    for letter in string_to_encrypt:
        upper_str_index = ""
        lower_str_index = ""
        if letter in upper_str:
            index = upper_str.find(letter)
            upper_str_index = upper_str[index:] + upper_str[:index]
            caesar_str += upper_str_index[step]
        elif letter in lower_str:
            index = lower_str.find(letter)
            lower_str_index = lower_str[index:] + lower_str[:index]
            caesar_str += lower_str_index[step]
        else:
            caesar_str += letter
    return caesar_str

def decrypting(upper_str, lower_str, step):
    caesar_str = ""
    for letter in string_to_decrypt:
        upper_str_index = ""
        lower_str_index = ""
        if letter in upper_str:
            index = upper_str.find(letter)
            upper_str_index = upper_str[index + 1:] + upper_str[:index + 1]
            caesar_str += upper_str_index[-step - 1]
        elif letter in lower_str:
            index = lower_str.find(letter)
            lower_str_index = lower_str[index + 1:] + lower_str[:index + 1]
            caesar_str += lower_str_index[-step - 1]
        else:
            caesar_str += letter
    return caesar_str

def check():
    int_check = int(input("Введите 1 или 2: "))
    while True:
        if int_check == 1 or int_check == 2:
            return int_check
        else:
            print("Такой вариант недоступен")
            int_check = int(input("Введите 1 или 2: "))

russian_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
russian_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
english_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
english_lower = 'abcdefghijklmnopqrstuvwxyz'

print("Это программа для шифровки и дешифровки с использованием шифра цезаря")
language = input("Выберите язык? ru - Русский , en - Английский: ")
while True:
    if language not in "en ru":
        language = input("Выберите язык? ru - Русский , en - Английский: ")
    else:
        break

print("Что бы вы хотели сделать? 1 - Зашифровать, 2 - Дешифровать: ")
question = check()
if question == 1:
    string_to_encrypt = input("Введите строку ,которую хотите зашифровать: ")
    step = int(input("Введите шаг шифровки: \n0 - 33 для русского языка и 0 - 26 для английского: "))
    if language == "en":
        if step == 26:
            step = 0
        caesar = encrypting(english_upper, english_lower, step)
    elif language == "ru":
        if step == 33:
            step = 0
        caesar = encrypting(russian_upper, russian_lower, step)
    print("Зашифрованная строка:", caesar)
elif question == 2:
    string_to_decrypt = input("Введите строку ,которую хотите дешифровать: ")
    print("Знаете ли вы шаг шифровки? 1 - если знаете; 2 - если не знаете: ")
    difficulty = check()
    if difficulty == 1:
        step = int(input("Введите шаг шифровки: "))
        if language == "en":
            caesar = decrypting(english_upper, english_lower, step)
        elif language == "ru":
            caesar = decrypting(russian_upper, russian_lower, step)
        print("Дешифрованная строка:", caesar)
    elif difficulty == 2:
        print("\nПрограмма будет выводить результаты подряд, \nСледуйте указаниям!")
        if language == "en":
            for step in range(26):
                caesar = decrypting(english_upper, english_lower, step)
                print("\nДешифрованная строка:", caesar)
                print("1 - если результат верен, 2 - если результат не верен: ")
                result = check()
                if result == 1:
                    print("Отлично!")
                    break
                if result == 2:
                    continue
        elif language == "ru":
            for step in range(34):
                caesar = decrypting(russian_upper, russian_lower, step)
                print("\nДешифрованная строка:", caesar)
                print("1 - если результат верен, 2 - если результат не верен: ")
                result = check()
                if result == 1:
                    print("Отлично!")
                    break
                if result == 2:
                    continue
