def main():
    import sys
    N=int(sys.stdin.readline())
    P=list(map(int,sys.stdin.readline().split()))
    now=0
    st=set()
    for i in range(N):
        if P[i]==now:
            while True:
                now+=1
                if now not in st:
                    break
        st.add(P[i])
        print(now)

main()