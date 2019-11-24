# a + b + c = 1000
# a^2 + b^2 = c^2
#
#a = r + s;  b = r + t; c = r + s + t
# 3r + 2s + 2t = 1000
#r^2 = 2st => (r^2)/2 = st

# (r + s)^2 + (r + t)^2 = (r + s + t)^2

def triplets(target):
    r = 6
    found = False
    count = 0
    while not found:
        s = 1
        p = (r**2)/2
        while s < r:
            count += 1
            if p % s == 0:
                t = int(p / s)
                a = r + s
                b = r + t
                c = r + s + t
                if (a + b + c) == target:
                    print(f"a = {a}, b = {b}, c = {c}, (a+b+c)={a+b+c}, (abc)={a*b*c}, r={r}, s={s}, t={t}")
                    found = True
            s += 1
        r += 2
    print(f"Loop counter: {count}")


triplets(1000)








