def main():
    import sys
    X,Y=list(map(int,sys.stdin.readline().split()))
    if Y%2==0 and 2*X<=Y and Y<=4*X:
        print('Yes')
    else:
        print('No')

main()