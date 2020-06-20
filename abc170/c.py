def main():
    import sys
    X,N=list(map(int,sys.stdin.readline().split()))
    P=list(map(int,sys.stdin.readline().split()))
    if not P:
        print(X)
        return
        
    P.sort()
    diff=10**5
    cand=0
    for i in range(min(X,min(P))-1,max(X,max(P))+2):
        if i not in P:
            d=abs(X-i)
            if d<diff:
                diff=d
                cand=i
    print(cand)


main()