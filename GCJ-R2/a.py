import sys
def solve():
    x,y=list(map(int,sys.stdin.readline().split()))
    lim=9
    def dfs(now,path):
        if now==(x,y):
            return path

        L=[]
        if -lim<now[1]<lim:
            N=dfs((now[0],now[1]+2**len(path)),path+'N')
            if N!=None:
                L.append(len(N))
            else:
                L.append(10**9)
            S=dfs((now[0],now[1]-2**len(path)),path+'S')
            if S!=None:
                L.append(len(S))    
            else:
                L.append(10**9)    
        else:
            L+=[10**9,10**9]
        if -lim<now[0]<lim:
            E=dfs((now[0]+2**len(path),now[1]),path+'E')
            if E!=None:
                L.append(len(E))    
            else:
                L.append(10**9)     
            
            W=dfs((now[0]-2**len(path),now[1]),path+'W')
            if W!=None:
                L.append(len(W))    
            else:
                L.append(10**9)     
            
            if min(L)==10**9:
                return None
        else:
            L+=[10**9,10**9]


        if min(L)==10**9:
            return None

        if min(L)==L[0]:
            return N
        elif min(L)==L[1]:
            return S
        elif min(L)==L[2]:
            return E
        else:
            return W
    
    t=dfs((0,0),'')
    if t:
        return "".join(t)
    else:
        return 'IMPOSSIBLE'

def main():
    T=int(input())
    for case in range(1,T+1):
         print('Case #{}: {}'.format(case,solve()))

main()