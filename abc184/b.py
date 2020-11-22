def main():
    import sys
    N,X=list(map(int,sys.stdin.readline().split()))
    lst=[1 if x=='o' else 0 for x in sys.stdin.readline().strip()]
    for i in lst:
        if i:
            X+=1
        else:
            X=max(0,X-1)
    print(X)
if __name__ == "__main__":
    main()