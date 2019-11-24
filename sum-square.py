def square_of_sum(n):
    return (n * (n + 1)/2.0)**2

def sum_of_square(n):
    sum = 0
    for n in range(1, n+1):
        sum += n ** 2
    return sum


# print(f"The sum of the square of 1-10 is: {sum_of_square(10)}")
# print(f"The sum of the square of 1-100 is: {sum_of_square(100)}")
# print(f"The square of the sum of 1-10 is: {square_of_sum(10)}")
# print(f"The square of the sum of 1-100 is: {square_of_sum(100)}")
diff = square_of_sum(100) - sum_of_square(100)
print(f"The difference is: {diff}")