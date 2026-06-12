def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
def print_even_message(number):
    if is_even(number):
        print(f"{number} juft son.")
    else:
        print(f"{number} toq son.")
def main():
    num = int(input("Son: "))
    print_even_message(num)
    
main()