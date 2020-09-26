def main():
    import sys
    A,B,C,D=list(map(int,sys.stdin.readline().split()))
    if C<=B and A<=D:
        print('Yes')
    else:
        print('No')
main()