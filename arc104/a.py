def main():
    import sys
    A,B=list(map(int,sys.stdin.readline().split()))
    print((A+B)//2,A-(A+B)//2)

main()