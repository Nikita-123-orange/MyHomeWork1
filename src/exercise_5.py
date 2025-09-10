from tqdm import tqdm
import time

def main():
    max_num = 30 #Предел числа, которое можно ввести
    try:
        num = int(input(f"Введите число от 1 до {max_num}: "))
        if num < 1 or num > max_num:
            print(f"Ошибка: число должно быть в диапазоне от 1 до {max_num}.")
            return
    except:
        print(f"Похоже вы ввели не число")

    factorial = 1
    print(f"Вычисляем факториал числа {num} с прогрессом:")
    for i in tqdm(range(1, num + 1)):
        factorial *= i
        time.sleep(0.05)  # задержка для наглядности прогресс-бара

    print(f"Факториал числа {num} равен: {factorial}")

if __name__ == "__main__":
    main()