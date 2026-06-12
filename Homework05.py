def check_guess(secret_number, guess):
    if guess < secret_number:
        return "kiritilgan son kichik!"
    elif guess > secret_number:
        return "kiritilgan son katta!"
    else:
        return "Togri!"
def print_result(is_correct):
    if is_correct:
        print("Togri!")
    else:
        print("Iltimos qaytadan urinib ko'ring!")
def main():
    secret_number = 42
    guess = int(input("Taxmin qiling: "))
    result = check_guess(secret_number, guess)
    print(result)
    is_correct = (result == "Togri!")
    print_result(is_correct)
main()