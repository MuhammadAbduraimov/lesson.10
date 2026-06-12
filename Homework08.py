def c_to_f(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
def main():
    choice = input("1: C to F, 2: F to C: ")
    if choice == "1":
        celsius = float(input("Celsius: "))
        fahrenheit = c_to_f(celsius)
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == "2":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = f_to_c(fahrenheit)
        print(f"{fahrenheit}°F = {celsius}°C")
    else:
        print("Noto'g'ri tanlov.")
main()