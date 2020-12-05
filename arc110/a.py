def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def main():
    import sys
    from collections import defaultdict
    N=int(sys.stdin.readline())
    res=1
    dic=defaultdict(int)
    for i in range(2,N+1):
        for a,b in factorization(i):
            dic[a]=max(b,dic[a])
    res=1
    for key in dic:
        res*=key**dic[key]
    print(res+1)



if __name__=='__main__':
    main()