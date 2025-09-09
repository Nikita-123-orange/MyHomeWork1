from tqdm import tqdm
import time

def main():
    n = int(input("Введите число от 1 до 30: "))
    if n < 1 or n > 30:
        print("Ошибка: число должно быть в диапазоне от 1 до 30.")
        return

    factorial = 1
    print(f"Вычисляем факториал числа {n} с прогрессом:")
    for i in tqdm(range(1, n + 1)):
        factorial *= i
        time.sleep(0.05)  # задержка для наглядности прогресс-бара

    print(f"Факториал числа {n} равен: {factorial}")

if __name__ == "__main__":
    main()