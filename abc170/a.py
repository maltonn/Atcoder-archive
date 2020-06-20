def main():
    import sys
    L=list(map(int,sys.stdin.readline().split()))
    for i,x in enumerate(L):
        if x==0:
            print(i+1)
            return


main()