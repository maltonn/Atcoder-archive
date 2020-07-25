def main():
    import sys
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    dp=[[0]*1000 for _ in range(N)]
    for i in range(1000):
        if i>=A[0]:
            dp[0][i]=dp[0][i-A[0]]+A[0]
        else:
            dp[0][i]=0

    for day in range(1,N):
        for i in range(1000):
            if i>=A[day]:
                dp[day][i]=max(dp[day-1][i],dp[day-1][i-A[day]]+A[day],dp[day][i-A[day]]+A[day])
            else:
                dp[day][i]=dp[day-1][i]

    print(dp)
    print(dp[-1][-1])


main()