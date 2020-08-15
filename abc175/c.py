def main():
    import sys
    X,K,D=list(map(int,sys.stdin.readline().split()))
    X=abs(X)
    if X-K*D>=0:
        print(X-K*D)
    else:
        count=X//D
        now=X%D
        if (K-count)%2==0:
            print(now)
        else:
            print(abs(now-D))

main()