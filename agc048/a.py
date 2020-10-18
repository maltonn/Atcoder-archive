def Comp(a,b):#a>b か
    return tuple(a)>tuple(b)

def solve(L):
    M=[ord(x)-97 for x in 'atcoder']
    if Comp(L,M):
        return 0

    if not any(L):#全部a
        return -1
    
    mn=101
    for i in range(len(M)):
        for j in range(i,len(L)):
            if M[i]<L[j]:
                mn=min(mn,j-i)
            if M[i]==L[j]:
                pass

    return mn


def main():
    import sys
    T=int(sys.stdin.readline())
    for _ in range(T):
        S=sys.stdin.readline().strip()
        L=[ord(x)-97 for x in S]
        print(solve(L))

main()