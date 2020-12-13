def main():
    import sys
    N,M,T=list(map(int,sys.stdin.readline().split()))
    mx=N
    prev=0
    for i in range(M):
        a,b=list(map(int,sys.stdin.readline().split()))
        N-=a-prev
        prev=b
        if N<=0:
            print('No')
            return
        N=min(mx,N+(b-a))

    N-=(T-b)
    if N<=0:
        print('No')
    else:
        print('Yes')

if __name__ == "__main__":
    main()