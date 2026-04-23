import datetime
text = input("...")
with open("diary.txt", "a", encoding="utf-8")as f:
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = f"{date} - {text}"
    f.write(output)
print("Записано в щоденик!")