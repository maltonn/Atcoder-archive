def main():
    import sys
    N,K=list(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))
    L=[0]*N
    
    n=0
    for i in range(K,N):
        if A[i]<=A[n]:
            print('No')
        else:
            print('Yes')
        n+=1

main()