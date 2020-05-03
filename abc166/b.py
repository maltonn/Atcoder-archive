def main():
    import sys
    N,K=list(map(int,sys.stdin.readline().split()))
    st=set()
    for i in range(K):
        d=int(sys.stdin.readline())
        A=list(map(int,sys.stdin.readline().split()))
        st=st|set(A)
    print(N-len(st))
    
main()