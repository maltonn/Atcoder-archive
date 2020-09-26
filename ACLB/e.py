def main():
    import sys
    N,Q=list(map(int,sys.stdin.readline().split()))
    for i in range(Q):
        L,R,D=list(map(int,sys.stdin.readline().split()))
    S='1'*N
    mod=998244353
    m=int(S)%mod

main()