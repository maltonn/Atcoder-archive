def main():
    import sys
    from bisect import bisect_right

    N,M,K=list(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))
    B=list(map(int,sys.stdin.readline().split()))

    AS=[0]*N
    BS=[0]*M
    for i,a in enumerate(A):
        if i:
            AS[i]=AS[i-1]+a
        else:
            AS[i]=a

    for i,b in enumerate(B):
        if i:
            BS[i]=BS[i-1]+b
        else:
            BS[i]=b

    mx=bisect_right(BS,K)
    for i,sa in enumerate(AS):
        if K-sa>=0:
            p=bisect_right(BS,K-sa)
            mx=max(mx,i+p+1)

    print(mx)


main()