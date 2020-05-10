def main():
    import sys
    N,K=list(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))
    A=[1]+A
    route=[1]
    st=set()
    st.add(1)
    now=1
    while True:
        now=A[now]
        if now in st:
            break
        route.append(now)
        st.add(now)
    
    idx=route.index(now)
    if K-idx+1>0:
        if len(route)-1!=idx:
            print(route[idx-1+(K-idx+1)%(len(route)-idx)])
        else:
            print(route[-1])
    else:
        print(route[K])
    

main()