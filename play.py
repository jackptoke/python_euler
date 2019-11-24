questions = ["name", "quest", "favourite colour"]
answers = ["lancelot", "the holy grail", "blue"]

for q, a in (zip(reversed(questions), reversed(answers))):
    print(f"what is your {q}? It is {a}.")