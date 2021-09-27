x = int(input("x 숫자를 입력하세요 : "))
es = float(input("es 숫자를 입력하세요 : "))
maxidx = int(input("MaxIter 숫자를 입력하세요 : "))

def exp(x, es, maxidx):
    idx = 1
    sol = 1
    ea = 100
    fac = 1

    while True:
        solold = sol
        fac = fac * idx
        sol = sol + x**idx / fac
        idx += 1
        if sol != 0 :
            ea = abs((sol-solold)/sol) * 100

        print("idx=",idx," ea=",ea," es=",es, " sol=",sol)

        if ea <= es or idx>=maxidx :
            return sol

print(exp(x,es,maxidx))