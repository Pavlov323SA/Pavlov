temperatures = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]

max_temp = max(temperatures)
min_temp = min(temperatures)
average_temp = sum(temperatures) / len(temperatures)

above_average = 0
for temp in temperatures:
    if temp > average_temp:
        above_average += 1

sorted_temps = sorted(temperatures)

fahrenheit_temps = []
for temp in temperatures:
    fahrenheit = temp * 9/5 + 32
    fahrenheit_temps.append(round(fahrenheit, 1))

print("Температуры:", temperatures)
print("Максимальная:", max_temp, "°C")
print("Минимальная:", min_temp, "°C")
print("Средняя:", round(average_temp, 1), "°C")
print("Дней выше средней:", above_average)
print("Отсортированные температуры:", sorted_temps)
print("Температуры в Фаренгейтах:", fahrenheit_temps)