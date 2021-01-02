def main():
    import sys
    A,B=list(map(int,sys.stdin.readline().split()))
    A=str(A)
    B=str(B)
    sa=0
    sb=0
    for a in A:
        sa+=int(a)
    for b in B:
        sb+=int(b)
    
    print(max(sa,sb))

if __name__ == "__main__":
    main()