fio = input("Введите ФИО через пробел: ")

parts = fio.split()

print("Фамилия:", parts[0].upper())
print("Имя:", parts[1].upper())
print("Отчество:", parts[2].upper())