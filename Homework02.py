def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


def main():
    current_year = int(input("Hozirgi yil: "))
    birth_year = int(input("Tug'ilgan yil: "))

    age = calculate_age(current_year, birth_year)
    print(f"Sizning yoshingiz: {age}")
    if age < 18:
        print("Siz voyaga yetmagan ekansiz.")
    elif age >= 18 :
        print("Siz voyaga yetgansiz.")

        

main()
