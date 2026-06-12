def is_valid_phone_number(phone: str) -> bool:
    if len(phone) == 9 and phone.isdigit():
        return True
    else:
        return False
def main():
    phone_number = input("Telefon raqamingizni kiriting (9 ta raqam): ")
    if is_valid_phone_number(phone_number):
        print("Telefon raqami to'g'ri.")
    else:
        print("Telefon raqami noto'g'ri. Iltimos, 9 ta raqam kiriting.")
main()