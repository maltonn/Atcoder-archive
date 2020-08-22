def main():
    import sys
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    mx=0
    h=0
    for a in A:
        if a<mx:
            h+=mx-a
        else:
            mx=a
    print(h)

main()