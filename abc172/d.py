def main():#no-sub
    import sys
    N=int(sys.stdin.readline())
    r=0
    for i in range(1,N+1):
        r+=(i+N-N%i)*(N//i)//2
    print(r)
main()