def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

gcd = lambda a, b: a if b==0 else gcd(b, a%b)

num1 = 48
num2 = 18
print("ЕҮОБ", num1, "и", num2, ":", gcd(num1, num2))


