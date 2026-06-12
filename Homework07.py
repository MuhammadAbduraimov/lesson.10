def ask_question(question: str, answer: str):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("To'g'ri javob!")
    else:
        print("Noto'g'ri javob. To'g'ri javob: " + answer)
        def check_answer(user_answer: str, correct_answer: str) -> bool:
            return user_answer.lower() == correct_answer.lower()
def main():
    ask_question("O'zbekiston poytaxti qaysi?", "Toshkent")
    ask_question("Dunyoning eng baland tog'i qaysi?", "Everest")
    ask_question("Python dasturlash tili kim tomonidan yaratilgan?", "Guido van Rossum")
main()