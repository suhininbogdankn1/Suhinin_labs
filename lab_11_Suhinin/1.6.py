with open("text.txt", "r", encoding="utf-8") as f:
    text = f.readlines()
maxl = 0
txt = ""
for line in text:
    line = line.replace("\n", "")
    line = line.replace(".","")
    line = line.split()
    for word in line:
        if len(word) > maxl:
            maxl = len(word)
            txt = word
print(f"Найдовше слово: '{txt}' - {maxl} символів")

