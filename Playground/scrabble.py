def word_ranking(input_str):
    words = input_str.lower().split()
    alphabet = 'a'
    alpha_score = {}
    for score in range(1, 27):
        alpha_score[alphabet] = score
        alphabet = chr(ord(alphabet) + 1)

    # print(alpha_score)
    # print(words)

    highest = 0
    result = ''
    for word in words:
        total = 0
        for a in list(word):
            total += alpha_score[a]
        if total > highest:
            highest = total
            result = word

    return (result, highest)

result = word_ranking("Say hello to your new zebra world")
print(f"The word is : {result[0]}")
print(f"The score is : {result[1]}")
