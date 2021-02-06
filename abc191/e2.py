from heapq import heappush, heappop

def dijkstra(n,adj,start,end=None,both_direction=True):#both_direction: True:無向グラフ 　False:有向グラフ
    n+=1
    
    INF = 10 ** 15
    dist = [INF] * n
    hq = [(0, start)] # (distance, node)
    dist[start] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    if end!=None:
        return dist[end]
    else:
        return dist


def main():
    import sys
    INF=10**15
    N,M=list(map(int,sys.stdin.readline().split()))
    nodes=[]
    st=set()#辺が一つでもが張られているノード

    quick_root=[INF]*N
    adj=[[] for _ in range(M)]
    for i in range(M):
        a,b,c=map(int,sys.stdin.readline().split())
        st.add(a-1)
        st.add(b-1)
        adj[a-1].append((b-1,c))
        #nodes.append((a-1,b-1,c))
        if a==b:
            quick_root[a-1]=min(c,quick_root[a-1])
    

    L=[[INF]*N for _ in range(N)]#L[i][j] iからjまでの最短距離
    for start in range(N):
        if start in st:
            d = dijkstra(N,adj,start,both_direction=False)#nodes,始点,終点,無向グラフ
            L[start]=d

    for i in range(N):
        if i not in st:
            print(-1)
            continue


        mn=INF
        for j in range(N):
            if j not in st:
                continue

            if i!=j:
                dist=L[i][j]+L[j][i]
                mn=dist if dist<mn else mn
        
        dist=quick_root[i]
        mn=dist if dist<mn else mn

        if mn>=INF:
            print(-1)
        else:
            print(mn)


if __name__ == "__main__":
    main()