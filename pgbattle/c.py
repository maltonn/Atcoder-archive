def main():#WA
    import sys
    N,M,D=list(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))
    A.sort()
    dic={}
    mod=10**9+7
    for a in A:
        if a%D in dic:
            dic[a%D].append(a)
        else:
            dic[a%D]=[a]
    res=N*(N//D+1)-D*(N//D)*(N//D+1)//2

    for key in dic:
        ok=0
        lst=dic[key]
        lst2=[lst[i]-lst[i-1] if i else lst[i] for i in range(len(lst))]
        lst2.append(N-lst[-1])
        for k in lst2:
            if k%D==0:
                t=k//D-1
            else:
                t=k//D
            ok+=(t+1)*t//2
        res-=((N+1-key)//D)*((N+1-key)//D +1)//2
        res+=ok

    print(res)

main()