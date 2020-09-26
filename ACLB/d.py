def main():#late AC
    import sys
    from bisect import bisect_left
    N,K=list(map(int,sys.stdin.readline().split()))
    A=[0]*N
    for i in range(N):
        A[i]=int(sys.stdin.readline())

    dp=[0]*(N+1)
    dp[0]=1
    if abs(A[0]-A[1])<=K:
        dp[1]=2
    else:
        dp[1]=1
    
    for i in range(2,N):
        mx=1
        for j in range(1,105):
            if i-j<0:
                break
            if abs(A[i-j]-A[i])<=K:
                mx=max(mx,dp[i-j]+1)

        dp[i]=mx

    print(max(dp))


main()