def main():
    import sys
    N,S,D=list(map(int,sys.stdin.readline().split()))
    flag=False
    for i in range(N):
        X,Y=list(map(int,sys.stdin.readline().split()))
        if X<S and D<Y:
            flag=True

    if flag:
        print('Yes')
    else:
        print('No')
    
if __name__ == "__main__":
    main()