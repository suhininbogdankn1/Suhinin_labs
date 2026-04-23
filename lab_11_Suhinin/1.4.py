import random
edge1 = 0
edge2 = 0
edge3 = 0
edge4 = 0
edge5 = 0
edge6 = 0
for gran in range (0, 1000):
    roll = random.randint(1, 6)
    if roll == 1:
        edge1 += 1
    elif roll == 2:
        edge2 += 1
    elif roll == 3:
        edge3 += 1
    elif roll == 4:
        edge4 += 1
    elif roll == 5:
        edge5 += 1
    elif roll == 6:
        edge6 += 1
print(f"Грань 1: {edge1/1000*100:.1f}%\nГрань 2: {edge2/1000*100:.1f}%\nГрань 3: {edge3/1000*100:.1f}%\nГрань 4: {edge4/1000*100:.1f}%\nГрань 5: {edge5/1000*100:.1f}%\nГрань 6: {edge6/1000*100:.1f}%")