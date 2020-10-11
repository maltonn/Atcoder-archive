def main():
    import itertools
    import sys
    A,B,C,D=list(map(int,sys.stdin.readline().split()))
    X=(A+B+C+D)//2
    if (A+B+C+D)%2==1:
        print('No')
        return

    lst=[
        A,
        B,
        C,
        D,
        A+B,
        A+C,
        A+D,
        B+C,
        B+D,
        C+D,
        A+B+C,
        A+B+D,
        A+C+D,
        B+C+D,
    ]
    if X in lst:
        print('Yes')
    else:
        print('No')

main()