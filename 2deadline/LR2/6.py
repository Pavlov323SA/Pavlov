n = int(input("Введите число n: "))

matrix = [[0] * n for _ in range(n)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y = n // 2, n // 2
num = 1
step = 1
dir_index = 0

if n % 2 == 0:
    x -= 1
    y -= 1

matrix[x][y] = num
num += 1

while num <= n * n:
    for _ in range(2):
        dx, dy = directions[dir_index]
        for _ in range(step):
            if num > n * n:
                break
            x += dx
            y += dy
            if 0 <= x < n and 0 <= y < n:
                matrix[x][y] = num
                num += 1
        dir_index = (dir_index + 1) % 4
    step += 1

for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]:2d}", end=" ")
    print()