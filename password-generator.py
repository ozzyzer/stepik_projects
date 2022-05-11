import random

def add_string(answer, argument):
    if answer.lower() == "да":
        return argument
    else:
        return ""

def generate_password(chars, password_length):
    password_list = random.sample(chars, password_length)
    return "".join(password_list)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
punctuation = '!#$%&*+-=?@^_'
chars = ''

print("Эта программа помогает сгенерировать пароль или конкретное количество паролей на основании требований, составленных пользователем")
print("Далее даны требованию к паролю: \nОтвет должен содержать наруральное число")
quantity = int(input("\nСколько паролей сгенерировать? "))
password_length = int(input("Длина одного пароля? "))
print("\nНапишите да/Да ,если хотите добавить и нет/Нет , если не хотите")

numbers = input("Включать ли цифры? ")
chars += add_string(numbers, digits)

uppercase_letters_add = input("Включать ли прописные буквы? ")
chars += add_string(uppercase_letters_add, uppercase_letters)

lowercase_letters_add = input("Включать ли строчные буквы? ")
chars += add_string(lowercase_letters_add, lowercase_letters)

punctuation_add = input("Включать ли знаки пунктуации? ")
chars += add_string(punctuation_add, punctuation)

VCC = input("Включать ли неоднозначные символы \'il1Lo0O\'? ")
if VCC.lower() == "нет":
    for letter in 'il1Lo0O':
        chars = chars.replace(letter, "")

while password_length > len(chars):
    print("\nСлишком большая длина пароля \nПароль должен быть меньше:", len(chars))
    password_length = int(input("Новая длина пароля: "))

print()
for passwords in range(quantity):
    password = generate_password(chars, password_length)
    print("Ваш пароль:", password)
