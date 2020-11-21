def Factorial(x,mod):
    res=1
    for i in range(1,x+1):
        res*=i
        res%=mod
    return res

def Fib(N,mod):
    L=[0]*N
    L[0]=1
    L[1]=1
    for i in range(2,N):
        L[i]=(L[i-1]+L[i-2])%mod

    return L[-1]



def main():
    debug=False
    import sys
    mod=10**9+7

    if debug:
        N=5
        I=input()
        Caa=I[0]
        Cab=I[1]
        Cba=I[2]
        Cbb=I[3]
    else:
        N=int(sys.stdin.readline())
        Caa=sys.stdin.readline().strip()
        Cab=sys.stdin.readline().strip()
        Cba=sys.stdin.readline().strip()
        Cbb=sys.stdin.readline().strip()
    Cs=Caa+Cab+Cba+Cbb
    
    if debug:
        dic={
            'AA':Caa,
            'AB':Cab,
            'BA':Cba,
            'BB':Cbb,
        }
        s='AB'
        def dfs(s):
            if len(s)==N:
                st.add(s)
                return

            for i in range(len(s)-1):
                dfs(s[:i+1]+dic[s[i:i+2]]+s[i+1:])
            

        st=set()
        dfs(s)
        print(len(st))

    if N==2:
        return 1

    if Cab=='A' and Caa=='A':#4
        return 1
    
    if Cab=='B' and Cbb=='B':#4
        return 1

    if Cs in ['ABBA','BAAA','BAAB','BBBA']:
        return Fib(N-1,mod)

    if Cs in ['ABAA','BABA','BABB','BBAA']:
        return pow(2,N-3,mod)
    




print(main())