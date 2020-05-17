def pow(x, n, m):
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
            K %= m
        x *= x
        x %= m
        n //= 2

    return (K * x) % m
def main():
    import sys
    from collections import Counter
    mod=1000000007
    N=int(sys.stdin.readline())
    L=[0]*N
    st=set()
    for i in range(N):
        A,B=list(map(int,sys.stdin.readline().split()))
        

    r=0

    print(r-1)#全部0っていうのは除く

main()