# Euclidean Algorithm to find gcd

def gcd(a,b):
    while a % b != 0: a, b = b, a % b
    return b

a = int(raw_input("What is the larger number? "))
b = int(raw_input("What is the smaller number? "))
#gcd = gcd(a,b) woah, woah, woah. This is really stupid - it overwrites the function
print(gcd(a,b))
