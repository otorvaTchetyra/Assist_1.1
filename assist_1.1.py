from datetime import datetime

def get_greeting():
    current_hour = datetime.now().hour
    
    if 6 <= current_hour < 12:
        return "Доброе утро!"
    elif 12 <= current_hour < 18:
        return "Добрый день!"
    elif 18 <= current_hour < 22:
        return "Добрый вечер!"
    else:
        return "Доброй ночи!"

def chat():
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ["выход", "пока", "стоп"]:
            print("Бот: До свидания!")
            break
        else:
            greeting = get_greeting()
            print(f"Бот: {greeting} Вы сказали: {user_input}")

if __name__ == "__main__":
    chat()

#Описание программы:
#Функция get_greeting:

#Определяет текущее время с помощью datetime.now().
#В зависимости от времени суток, возвращает соответствующее приветствие:
#Утро: 6:00 - 11:59
#День: 12:00 - 17:59
#Вечер: 18:00 - 21:59
#Ночь: 22:00 - 5:59
#Функция chat:

#Запускает бесконечный цикл, в котором бот отвечает на сообщения пользователя.
#Если пользователь вводит одно из ключевых слов ("выход", "пока", "стоп"), программа завершает работу.
#В остальных случаях бот отвечает, используя приветствие в зависимости от времени суток и добавляет текст сообщения пользователя.
