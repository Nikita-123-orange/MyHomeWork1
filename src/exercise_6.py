from tqdm import tqdm
import time

def main():
    #Ограничение введеного числа из за ограничения вычислительных мощностей
    max_num = 50
    try:
        n = int(input(f"Введите число от 1 до {max_num}: "))
        if n < 1 or n > max_num:
            print(f"Число должно быть в диапазоне от 1 до {max_num}.")
            return
    except:
        print("Похоже вы ввели не число")
    fib = [0, 1]  # базовые значения

    print(f"Вычисляем {n}-е число Фибоначчи с прогрессом:")
    for i in tqdm(range(2, n + 1)):
        fib.append(fib[i - 1] + fib[i - 2])
        time.sleep(0.05)  # небольшая задержка для наглядности прогресса

    print(f"{n}-е число Фибоначчи: {fib[n]}")

if __name__ == "__main__":
    main()