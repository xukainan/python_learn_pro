num = 1
while num < 10:
    if num >= 5:
        break
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1