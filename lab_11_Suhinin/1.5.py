with open('poem.txt', 'r',) as f:
    poem = f.readlines()
a = 0
b = 0
for word in poem:
    word = word.strip()
    word = word.split()
    b += 1
    for char in word:
        a += 1
print(f"Рядків: {b}")
print(f"Слів: {a}")