def main():
    import sys
    N,X=list(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))

    L=[]
    for a in A:
        if a!=X:
            L.append(a)
    print(' '.join([str(x) for x in L]))

if __name__ == "__main__":
    main()