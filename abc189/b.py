def main():
    import sys
    N,X=list(map(int,sys.stdin.readline().split()))
    now=0
    flag=False
    for i in range(N):
        v,p=list(map(int,sys.stdin.readline().split()))
        now+=v*p
        if now>X*100:
            flag=True
            print(i+1)
            return
            
    if not flag:
        print(-1)

if __name__ == "__main__":
    main()