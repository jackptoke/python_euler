scores = [78, 86, 98, 68, 38, 99, 89, 78, 86, 48]
names = ["Jack", "Maung", "Eh Soe", "Eh Paw", "Saw Thoo", "Ker Chaw", "Podi", "Pahdi", "Sah Wah", "Saw Mya"]

total = sum(scores)
average = total/len(scores)
i = 0

while i < len(scores):
    print(f"{names[i]} => {scores[i]}")
    i = i + 1

for x in names:
   print(f"Name: {x}")

print(f"The average score: {average}")
