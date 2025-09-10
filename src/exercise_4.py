#Импорт библиотек
from tqdm import tqdm

def main():
    number_max=10 #Число, до которого будут выводится четные числа
    for num_for_print in tqdm(range(2, number_max+1, 2), desc=f"Вывод четных чисел до {number_max}"): 
        print(num_for_print)
    

if __name__ == "__main__":
    main()