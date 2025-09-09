import importlib
import sys
import os

def main():
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    """Основная функция запуска упражнений"""
    while True:
        # Меню выбора
        print("\n" + "="*35)
        print("ВЫБЕРИТЕ УПРАЖНЕНИЕ (1-6):")
        print("="*35)
        print("1 - Упражнение 1")
        print("2 - Упражнение 2")
        print("3 - Упражнение 3")
        print("4 - Упражнение 4")
        print("5 - Упражнение 5")
        print("6 - Упражнение 6")
        print("0 - Выход")
        print("="*35)
        
        # Получаем выбор
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
    """Запускает выбранное упражнение"""
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