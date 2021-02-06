def main():
    import sys
    V,T,S,D=list(map(int,sys.stdin.readline().split()))
    if V*T<=D<=V*S:
        print('No')
    else:
        print('Yes')

    
if __name__ == "__main__":
    main()