text = input("Введите текст: ")

words = text.split()
clean_words = []
for word in words:
    clean_word = ""
    for char in word:
        if char.isalpha():
            clean_word += char.lower()
    if clean_word:
        clean_words.append(clean_word)

if clean_words:
    longest_word = clean_words[0]
    shortest_word = clean_words[0]
    
    for word in clean_words:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortest_word):
            shortest_word = word
    
    total_length = 0
    for word in clean_words:
        total_length += len(word)
    average_length = total_length / len(clean_words)
    
    word_count = {}
    for word in clean_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    sorted_words = []
    for word, count in word_count.items():
        sorted_words.append((word, count))
    
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i][1] < sorted_words[j][1]:
                sorted_words[i], sorted_words[j] = sorted_words[j], sorted_words[i]
    
    top_words = sorted_words[:5]
    
    print("Самое длинное слово:", longest_word)
    print("Самое короткое слово:", shortest_word)
    print("Средняя длина:", round(average_length, 1))
    print("Топ-5 слов:", top_words)
else:
    print("Нет слов для анализа")