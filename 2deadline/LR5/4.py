from random import randint

random_num = randint(1, 100)

while True:
    guess = int(input("Угадайте число от 1 до 100: "))
    
    if guess == random_num:
        print("Угадал!")
        break
    elif guess > random_num:
        print("Меньше")
    else:
        print("Больше")
