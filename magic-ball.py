import random

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай", "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет", "Определённо да", "Знаки говорят - да", "Сейчас нельзя предсказать", "Перспективы не очень хорошие", "Можешь быть уверен в этом", "	Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print("Привет, я магический  шар , и я знаю ответ на любой ваш вопрос!")
name = input("Как вас зовут? ")
print("Привет," , name)

while True:
    print("Ты можешь задать любой вопрос или напиши \"Хватит вопросов\" ,чтобы закончить")
    question = input("Ваш вопрос: ")
    if question.lower() == "хватит вопросов":
        print("Возвращайся если возникнут вопросы!")
        break
    else:
        print(random.choice(answers))