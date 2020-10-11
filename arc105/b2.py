def main():#WA
    import sys
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    A.sort()
    mn=A[0]
    res=10**9+1

    st=set()
    for a in A[1:]:
        tmp=min(mn,a%mn)
        st.add(A%mn)
        if tmp==0:
            print(mn)
            return
        mn=tmp

    print(mn)


main()