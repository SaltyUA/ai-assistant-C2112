import random
import os
import json

#===================Hалаштування========================

NAME = "Ada"
DEFAULT_PERSONALITY = "Я - Ada, твій віртуальний асистент. Я можу розповісти жарт або просто привітати тебе."

def load_personality():
    if os.path.exists("persona.txt"):
        try:
            with open("persona.txt", "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    return text
        except Exception:
            pass
    return DEFAULT_PERSONALITY

PERSONALITY = load_personality()


#===================Функції для роботи з користувачем========================

def load_user():
    if os.path.exists("user.json"):
        try:
            with open("user.json", "r", encoding="utf-8") as f:
                text = f.read().strip()
                if not text:
                    return None
                data = json.loads(text)
                return data.get("name")
        except Exception:
            return None
    return None

def get_user():
    user = load_user()
    if user:
        return user
    else:
        name = input("Введіть ваше ім'я: ")
        while True:
            if not name.strip():
                print("Ім'я не може бути порожнім. Спробуйте ще раз.")
                name = input("Введіть ваше ім'я: ")
            else:
                with open("user.json", "w", encoding="utf-8") as f:
                    json.dump({"name": name}, f)
                return name

#===================Списки відповідей========================

greatings = [
    "Привіт! Як справи?",
    "Доброго дня! Чим можу допомогти?",
    "Вітаю! Що цікавого ти хочеш дізнатися?",
    "Привіт! Я тут, щоб допомогти тобі.",
    "Доброго ранку! Як я можу тобі допомогти?"
]

jokes = [
    "Чому комп'ютер ніколи не відчуває голоду? Бо він завжди має багато байтів!",
    "Чому програмісти не люблять природу? Бо там занадто багато багів!",
    "Як називається комп'ютер, який співає? А-нотація!",
    "Чому комп'ютер ніколи не відчуває втоми? Бо він завжди на енергії!"]

motivates =[
    "Ти можеш все, що забажаєш!",
    "Не бійся помилок, вони - шлях до успіху!",
    "Кожен день - це нова можливість стати кращим!",
    "Твоя сила в твоїй рішучості!",
    "Вір у себе, і ти зможеш досягти всього!",
]

fallbacks =[
    "Вибач, я не зовсім зрозумів. Можеш пояснити ще раз?",
    "Це цікаво, але я не впевнений, як на це відповісти.",
    "Можливо, ти маєш на увазі щось інше? Я не зовсім зрозумів.",
    "Це звучить цікаво, але я не можу знайти відповідь на це питання.",
    "Вибач, але я не можу відповісти на це. Можливо, спробуємо щось інше?",
]

empty =[
    "Ти нічого не написав. Спробуй ще раз.",
    "Здається, ти забув щось написати. Напиши мені щось.",
    "Я не отримав від тебе повідомлення. Напиши мені, будь ласка, щось.",
    "Ти нічого не написав. Можливо, ти хотів щось запитати?",
    "Здається, ти забув написати повідомлення. Напиши мені, будь ласка, щось.",
]

#===================Функції для отримання випадкових відповідей========================

def random_greating():
    return random.choice(greatings)

def random_joke():
    return random.choice(jokes)

def random_motivate():
    return random.choice(motivates)

def random_fallback():
    return random.choice(fallbacks)

def random_empty():
    return random.choice(empty)

#===================Функції для роботи з нотатками========================

def add_note():
    note = input("Введіть текст нотатки: ")
    if not note.strip():
        return "Нотатка не може бути порожньою."
    try:
        with open("notes.txt", "a", encoding="utf-8") as f:
            f.write(note + "\n")
        return "Нотатку успішно додано."
    except Exception as e:
        return f"Помилка при додаванні нотатки: {e}"
    

def read_note():
    if not os.path.exists("notes.txt"):
        return "Немає жодної нотатки."
    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            notes = f.readlines()
        if not notes:
            return "Немає жодної нотатки."
        formatted_notes = [f"{i+1}. {note.strip()}\n" for i, note in enumerate(notes)]
        return "Ось ваші нотатки:\n" + "".join(formatted_notes)
    except Exception as e:
        return f"Помилка при читанні нотаток: {e}"
    

def delete_note():
    if not os.path.exists("notes.txt"):
        return "Немає жодної нотатки для видалення."
    try:
        with open("notes.txt", 'w', encoding="utf-8") as f:
            f.write("")
        return "Всі нотатки успішно видалено."
    except Exception as e:
        return f"Помилка при видаленні нотаток: {e}"
    
#===================Функції для аналізу тексту========================

def analyze_text(text):
    t = text.lower()  
    if not t.strip():
        return "empty"
    if any(k in t for k in ("joke", "жарт", "сміх")):
        return "joke"
    if any(k in t for k in ("привіт", "доброго дня", "вітання", "привітання")):
        return "greeting"
    if any(k in t for k in ("мотивуй", "надихни", "підтримай", "мотивація")):
        return "motivate"
    if any(k in t for k in ("вийти", "вихід", "закрити", "завершити")):
        return "exit"
    if any(k in t for k in ("запиши нотатку", "створи нотатку", "записати нотатку", "збережи нотатку")):
        return "add note"
    if any(k in t for k in ("прочитай нотатку", "показажи нотатки", "показати нотатки", "переглянути нотатки")):
        return "read note"
    if any(k in t for k in ("видали нотатку", "видалити нотатку", "знищити нотатку", "стерти нотатку")):
        return "delete note"
    return "unknown"

#===================Функція для отримання відповіді========================

def get_response(text):
    tag = analyze_text(text)
    if tag == "empty":
        return random_empty()
    if tag == "greeting":
        return random_greating()
    if tag == "motivate":
        return random_motivate()
    if tag == "joke":
        return random_joke()
    if tag =="unknown":
        return random_fallback()
    if tag == "add note":
        return add_note()
    if tag == "read note":
        return read_note()
    if tag == "delete note":
        return delete_note()
    if tag == "exit":
        return "exit"


#===================Основна функція програми========================

def main():
    print(PERSONALITY)

    user_name = get_user()
    print(f"{NAME}: {user_name}, {random_greating()}! Готовий працювати. Якщо захочеш вийти напиши 'exit'")
    while True: 
        user = input("Ти: ")
        response = get_response(user)
        if response == "exit":
            print(f"{NAME}: До зустрічі! Гарного дня!")
            break
        print(f"{NAME}: {response}")

#======================Запуск програми========================

if __name__ == "__main__":
    main()    
    
