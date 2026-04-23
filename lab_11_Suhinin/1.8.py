with open("multiplication_table.txt", "w", encoding="utf-8") as f:
    for i in range(1,11):
        for j in range(1,11):
            text = f"{i}x {j} = {i*j}    "
            f.write(text)
        f.write("\n")
print("Виконано!")