def Comp(a,b):#a>b か
    return tuple(a)>tuple(b)

def solve(L):
    M=[ord(x)-97 for x in 'atcoder']
    if Comp(L,M):
        return 0

    if not any(L):#全部a
        return -1
    
    res=0
    K=[]
    for i in range(len(M)):
        for j in range(i,len(L)):
            if M[i]<=L[j-sum([j<=x for x in K])]:
                res+=i-j
                K.append(j)
                break

        
    return res


def main():
    import sys
    T=int(sys.stdin.readline())
    for _ in range(T):
        S=sys.stdin.readline().strip()
        L=[ord(x)-97 for x in S]
        print(solve(L))

main()