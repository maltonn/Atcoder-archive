def main():
    import sys
    N=int(sys.stdin.readline())
    out=0
    for i in range(1,N):
        out+=(N-1)//i
    print(out)

main()