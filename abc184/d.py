def main():
    import sys
    import numpy as np
    A,B,C=list(map(int,sys.stdin.readline().split()))
    dp=np.zeros((101,101,101))
    dp[100,:,:]=0
    dp[:,100,:]=0
    dp[:,:,100]=0
    for x in range(99,-1,-1):
        for y in range(99,-1,-1):
            for z in range(99,-1,-1):
                if x or y or z:#全部0は除く
                    dp[x,y,z]=x/(x+y+z)*(dp[x+1,y,z]+1) + y/(x+y+z)*(dp[x,y+1,z]+1) + z/(x+y+z)*(dp[x,y,z+1]+1)

    print(dp[A,B,C])

if __name__ == "__main__":
    main()