text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

if word in text:
    count = text.count(word)
    print(f"Слово '{word}' найдено в тексте")
    print(f"Количество вхождений: {count}")
else:
    print(f"Слово '{word}' не найдено в тексте")