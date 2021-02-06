def main():
    import sys
    H,W=list(map(int,sys.stdin.readline().split()))
    L=[[0]*W for _ in range(H)]
    for i in range(H):
        L[i]=[0 if x=='.' else 1 for x in list(sys.stdin.readline().strip())]
    res=0
    for i in range(H-1):
        for j in range(W-1):
            n=L[i][j]+L[i+1][j]+L[i][j+1]+L[i+1][j+1]
            res+=n%2

    print(res)

if __name__ == "__main__":
    main()