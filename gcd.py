

def gcd(a,b):
    c = a%b
    if c == 0:
        return b
    else :
        return gcd(b,c)

print(gcd(72345, 43215))