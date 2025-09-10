#Импорт библиотек
import importlib
import sys
import os

def main():
    #Нужно для того, чтоб все файлы из папки SRC можно было импртировать без указания полного пути src.<файл для вызова>
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    #Основная функция запуска упражнений
    while True:
        number_of_exercise = 6
        # Меню выбора
        print("\n" + "="*35)
        print("ВЫБЕРИТЕ УПРАЖНЕНИЕ (1-6):")
        print("="*35)
        number_max=6 #Число, до которого будут выводится четные числа
        for number_of_exercise in range(1, number_max+1, 1): 
            print(f"{number_of_exercise} - Упражнение {number_of_exercise}")
        print("0 - Выход")
        print("="*35)

        #Получаем выбор
        choice = input("Ваш выбор: ")

        # Обрабатываем выбор
        if choice == '0':
            print("До свидания! 👋")
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            # Запускаем выбранное упражнение
            run_exercise(choice)
        else:
            print("❌ Ошибка! Введите число от 0 до 6")

def run_exercise(ex_number):
    #Запускает выбранное упражнение
    try:
        # Импортируем и запускаем модуль упражнения
        module = importlib.import_module(f"exercise_{ex_number}")
        module.main()
    except ImportError:
        print(f"❌ Файл exercise_{ex_number}.py не найден!")
    except AttributeError:
        print(f"❌ Функция main() не найдена в exercise_{ex_number}.py")
    except Exception as e:
        print(f"❌ Ошибка при выполнении: {e}")

# Запуск программы
if __name__ == "__main__":
    main()