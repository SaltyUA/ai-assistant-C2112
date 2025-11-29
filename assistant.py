import random
import os

NAME = "Jarvis"
DEFAULT_PERSONALITY = "тактичний, веселий"

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

greatings = ["Привіт", "Вітаю", "Хай"]

jokes = ["Жарт 1", "Жарт 2", "Жарт 3"]

motivates =[]

fallbacks =[]

empty =[]

#===================RANDOMS============
def random_greating():
    return random.choice(greatings)

def random_joke():
    return random.choice(jokes)

#=================MAIN FUNC===============

def analyze_text(text):
    t = text.lower()  
    if not t.strip():
        return "empty"
    if any(k in t for k in ("joke", "жарт", "сміх")):
        return "joke"
    return "unknown"

def get_response(text):
    tag = analyze_text(text)
    if tag == "empty":
        return f"{NAME}: Ти нічого не написав. Спробуй ще раз"
    if tag == "joke":
        return random_joke()
    if tag =="unknown":
        return f"{NAME}: Я нічого не розумію, але ти сказав - {text}"

def main():
    print(f"{NAME}({PERSONALITY}): {random_greating()}! Готовий працювати. Якщо захочеш вийти напиши 'exit'")
    while True: 
        user = input("Ти: ")
        if user in "exit": 
            print(f"{NAME}: Бувай!")
            break
        print(get_response(user))

if __name__ == "__main__":
    main()    
    
