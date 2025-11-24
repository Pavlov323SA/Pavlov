text_lines = []
print("Введите текст (пустая строка для завершения):")

while True:
    line = input()
    if line == "":
        break
    text_lines.append(line)

full_text = " ".join(text_lines)
words = full_text.lower().split()

word_stats = {}

for word in words:
    clean_word = word.strip(".,!?;:")
    if clean_word in word_stats:
        word_stats[clean_word] += 1
    else:
        word_stats[clean_word] = 1

print(f"Статистика слов: {word_stats}")