def isPalindrome(strx):
    i = 0
    j = len(strx) - 1
    while i < j:
        if strx[i] != strx[j]:
            return False
        i += 1
        j -= 1

    return True

test = "asba"
# print(isPalindrome(test))
start = 999
found = False
largest = 0
x = 0
y = 0
while start > 100:
    stop = 999
    while stop > 100:
        n = start * stop
        if isPalindrome(str(n)):
            if n > largest:
                largest = n
                x = start
                y = stop
        stop -= 1
    start -= 1

print(f"The longest palindrome: {x} x {y} = {largest}")