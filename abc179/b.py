def main():
    import sys
    N=int(sys.stdin.readline())
    count=0
    for i in range(N):
        D1,D2=list(map(int,sys.stdin.readline().split()))
        if D1==D2:
            count+=1
        else:
            count=0
        if count==3:
            print('Yes')
            break
    else:
        print('No')

main()