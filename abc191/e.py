from heapq import heappush, heappop

def dijkstra(n,adj,start):
    INF = 10 ** 12
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

    return dist


def main():
    import sys
    INF=10**12
    N,M=list(map(int,sys.stdin.readline().split()))
    nodes=[]

    quick_root=[INF]*N
    counts=[0]*N
    adj=[[] for _ in range(N)]
    for i in range(M):
        a,b,c=map(int,sys.stdin.readline().split())
        adj[a-1].append((b-1,c))
        if a==b:
            quick_root[a-1]=c
        else:
            counts[a-1]+=1

    L=[[INF]*N for _ in range(N)]#L[i][j] iからjまでの最短距離
    for start in range(N):
        d = dijkstra(N,adj,start)#nodes,始点,終点,無向グラフ
        L[start]=d

    for i in range(N):
        mn=INF
        for j in range(N):
            if i==j:
                continue

            if L[i][j]==INF:
                continue
            
            if counts[i]==0:
                break

            counts[i]-=1


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