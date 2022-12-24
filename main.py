s = list()
while True:
    a = input().lower()
    if a == '':
        break
    else:
        s.append(a)

cats = 0
dogs = 0
for i in s:
    if "кошка" in i or "кот" in i:
        cats += 1
    if "собака" in i:
        dogs += 1
print("Котов: " + str(cats))
print("Собак " + str(dogs))
