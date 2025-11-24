n = int(input("Введите высоту пирамиды: "))

for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    
    left_part = ''
    for j in range(1, i + 1):
        left_part += str(j)
    
    right_part = ''
    for j in range(i - 1, 0, -1):
        right_part += str(j)
    
    print(spaces + left_part + right_part)