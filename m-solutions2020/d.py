def main():
    import sys
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    B=[0]*N

    money=1000
    kabu=0
    for i in range(N-1):
        if A[i]<A[i+1]:
            kabu+=money//A[i]
            money%=A[i]

        elif A[i]>A[i+1]:
            money+=kabu*A[i]
            kabu=0

    money+=kabu*A[-1]
    print(money)
    
main()