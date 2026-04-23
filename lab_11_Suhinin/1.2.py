import math
rad = int(input("Введіть радікс кола: "))
def calculate(radius):
    area = math.pi * radius ** 2
    circlelength = 2*math.pi * radius
    area = round(area,2)
    circlelength = round(circlelength,2)
    return (area,circlelength)
print(calculate(rad))