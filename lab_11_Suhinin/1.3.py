from datetime import date

year = int(input("Рік: "))
month = int(input("Місяць: "))
day = int(input("День: "))

today = date.today()
birth_date = date(year, month, day)

age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

days_ukr = [
    "понеділок", "вівторок", "середа",
    "четвер", "п'ятниця", "субота", "неділя"
]
weekday = days_ukr[birth_date.weekday()]

next_birthday = date(today.year, month, day)
if next_birthday <= today:
    next_birthday = date(today.year + 1, month, day)

days_until = (next_birthday - today).days

print(f"Вік: {age} років")
print(f"День народження: {weekday}")
print(f"Днів до наступного дня народження: {days_until}")