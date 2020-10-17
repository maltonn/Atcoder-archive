def main():
    import sys
    N=int(sys.stdin.readline())
    X=list(map(int,sys.stdin.readline().split()))
    M=0
    for x in X:
        M+=abs(x)
    print(M)

    U=0
    for x in X:
        U+=x**2
    print(U**(1/2))

    print(max(map(abs,X)))

main()