def f1():
    L=[2]
    for i in range(3,100):
        for j in L:
            if i%j==0:
                break
        else:
            L.append(i)

    res=1
    for i in L:
        res*=i
        if res>=10**15:
            break
        print(i,res)



a,b=162,125

#関数を定義
def gcd(a,b):
    if b == 1:
        return a
    else:
        return gcd(b,a%b)

print(gcd(a,b))
