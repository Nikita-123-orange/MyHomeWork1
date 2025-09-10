def main():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    summa = a + b
    if  (a + b) % 2==0:
        average = int((a+b)/2)#Если число целое, то будет формат числа без <.0>
    else:
        average = (a + b)/2
    # Проверяем деление на ноль для частного и остатка
    if b != 0:
        if a%b==0: 
            quotient = int(a / b) #Если число целое, то будет формат числа без <.0>
        else:
            quotient = a/b
        remainder = a % b
    else:
        quotient = "деление на ноль невозможно"
        remainder = "деление на ноль невозможно"

    print(f"Сумма: {summa}")
    print(f"Среднее значение: {average}")
    print(f"Частное (a / b): {quotient}")
    print(f"Остаток от деления (a % b): {remainder}")

    # Проверяем четность
    print(f"{a} {'четное' if a % 2 == 0 else 'нечетное'} число")
    print(f"{b} {'четное' if b % 2 == 0 else 'нечетное'} число")

if __name__ == "__main__":
    main()