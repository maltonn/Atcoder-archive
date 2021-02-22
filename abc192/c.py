def main():
    import sys
    N,K=list(map(int,sys.stdin.readline().split()))
    A=str(N)
    for i in range(K):
        A=str(int(''.join(sorted(list(A),reverse=True)))-int(''.join(sorted(list(A)))))
    print(A)

if __name__ == "__main__":
    main()