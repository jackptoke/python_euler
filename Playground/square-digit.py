def square_digit(number):
    nums = list(str(number))
    result = ""

    for n in nums:
        i = int(n)
        result += str(i*i)
    return result

print(square_digit(9119))