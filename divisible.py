found = False
n = 100
while not found:
    count = 0
    for x in range(2, 21):
        if n % x != 0:
            break
        count += 1
    if count == 19:
        found = True
    else:
        n += 1

print(f"The number is: {n}")