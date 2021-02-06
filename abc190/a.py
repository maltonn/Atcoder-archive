def main():
    import sys
    A,B,C=list(map(int,sys.stdin.readline().split()))
    B-=C
    if A>B:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == "__main__":
    main()