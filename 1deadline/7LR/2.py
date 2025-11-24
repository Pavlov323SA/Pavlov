password = input("Введите пароль: ")
confirm = input("Подтвердите пароль: ")

if password == confirm:
    auth = input("Введите пароль для авторизации: ")
    if auth == password:
        print("Access")
    else:
        print("Denied")
else:
    print("Пароли не совпадают")