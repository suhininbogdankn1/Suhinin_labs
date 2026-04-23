import random
import string

a = 0
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
alltogether = upper + lower + digits
password = []
for i in range(5):
    password.append(random.choice(upper))
    password.append(random.choice(lower))
    password.append(random.choice(digits))
    a += 1
    for j in range(5):
        password.append(random.choice(alltogether))
    random.shuffle(password)
    password = "".join(password)
    print(f"{a}. {password}")
    password = []



