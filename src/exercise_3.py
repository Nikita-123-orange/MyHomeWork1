def main():
    s = input("Введите строку: ")
    words = s.split()
    word_count = len(words)
    reversed_str = s[::-1]

    print(f"Количество слов: {word_count}")
    print(f"Развернутая строка: {reversed_str.strip()}") #Пробелы по краям не учитываются

if __name__ == "__main__":
    main()