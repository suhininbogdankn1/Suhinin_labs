with open("numbers.txt", "r", encoding="utf-8") as f:
    numbers = f.readlines()
suma = 0
for n in numbers:
    suma += int(n)
print(suma)