def main():
    import sys
    N,D=list(map(int,sys.stdin.readline().split()))
    count=0
    for i in range(N):
        x,y=list(map(int,sys.stdin.readline().split()))
        if x**2+y**2<=D**2:
            count+=1

    print(count)
main()