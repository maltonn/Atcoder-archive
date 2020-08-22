def main():
    import sys
    N,X,T=list(map(int,sys.stdin.readline().split()))
    print((N//X+(1 if N%X else 0))*T)

main()