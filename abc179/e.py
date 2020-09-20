

def main():#TLE 
    import sys
    st=set()
    N,X,M=list(map(int,sys.stdin.readline().split()))
    L=[]
    a=-1
    for i in range(N):
        a=pow(X,2<<(i-1) if i else 1,M)
        if a in st:
            break
        else:
            st.add(a)
            L.append(a)

    n=N
    if a+1:
        idx=L.index(a)
        res=sum(L[:idx])
        n-=idx

        s=sum(L[idx:])
        length=len(L)-idx
        res+=s*(n//length)
        res+=(sum(L[idx:idx+n%length]))
        print(res)
    else:
        print(sum(N))



main()
