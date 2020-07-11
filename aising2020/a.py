def main():
    import sys
    L,R,d=list(map(int,sys.stdin.readline().split()))
    print(R//d-(L-1)//d)

main()