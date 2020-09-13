def main():
    import sys
    a,b,c,d=list(map(int,sys.stdin.readline().split()))
    print(max(a*c,b*d,a*d,b*c))

main()