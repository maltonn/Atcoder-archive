def solve(N,A,B):
    pass

def main():
    import sys
    T=int(sys.stdin.readline())
    for i in range(T):
        N,A,B=list(map(int,sys.stdin.readline().split()))
        print(solve(N,A,B))

main()