str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

clean_str1 = str1.lower().replace(" ", "")
clean_str2 = str2.lower().replace(" ", "")

sorted_str1 = ''.join(sorted(clean_str1))
sorted_str2 = ''.join(sorted(clean_str2))

if sorted_str1 == sorted_str2:
    print("Строки являются анаграммами")
else:
    print("Строки не являются анаграммами")