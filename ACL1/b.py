def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr



def main():
    import sys
    N=int(sys.stdin.readline())
    F=factorization(2*N)
    def dfs(idx,now):
        print(idx,now)
        if idx==len(F):
            a=now
            b=2*N//now
            if a>=2 and (a*t-1)%b==0:
                return a-1
            else:
                return 10**15
        else:
            r1=dfs(idx+1,now*(F[idx][0]**F[idx][1]))
            r2=dfs(idx+1,now)
            return min(r1,r2)
    
    res=dfs(0,1)
    print(res)

main()


"""
    N=int(sys.stdin.readline())
    res=10**15+1
    if int(2*N**(1/2))*(int(2*N**(1/2))+1)==2*N:
        res=min(int(2*N**(1/2)),res)
    if int(N**(1/2))*(int(N**(1/2))+1)==N:
        res=min(int(N**(1/2)),res)
    if N%2==0:
        res=min(2*N-1,res)
 
    res=min(N-1,res)
    
    print(res)

"""