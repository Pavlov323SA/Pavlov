text = input("Введите текст: ")
replace_data = input("Введите что заменить и на что: ").split()
old_str, new_str = replace_data[0], replace_data[1]
result = text.replace(old_str, new_str)
print(result)