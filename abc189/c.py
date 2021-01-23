def main():#WA #反例：5 4 3 2 1 2
    import sys
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    L=[]
    mx=0
    i=0
    while True:
        print(L,mx)
        if i==N:
            break
        a=A[i]
        if not L:
            L.append((a,i))
            i+=1
        elif L[-1][0]<=a:
            L.append((a,i))
            i+=1
        else:
            b,j=L.pop()
            mx=max(mx,(i-j)*b)

    while L:
        b,j=L.pop()
        mx=max(mx,(N-j)*b)

    print(mx)        

if __name__ == "__main__":
    main()