def main():
    import sys
    A,B,C,K=list(map(int,sys.stdin.readline().split()))
    o=0
    if K>=A:
        K-=A
        o+=A
    else:
        print(K)
        return

    if K>=B:
        K-=B
    else:
        print(o)
        return
    
    print(o-K)

main()