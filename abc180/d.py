def main():
    import sys
    X,Y,A,B=list(map(int,sys.stdin.readline().split()))
    res=0
    while X*A<X+B:
        X*=A
        res+=1
        if X>=Y:
            res-=1
            print(res)
            return
    res+=(Y-X)//B
    if (Y-X)%B==0:
        res-=1
    print(res)

main()