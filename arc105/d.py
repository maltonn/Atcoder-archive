from collections import Counter
def XOR(lst):
    res=0
    for a in lst:
        res^=a
    return res

def solve(N,A):
    #全皿のxor=0にしたら勝ち
    if N==1:
        return 'Second'
    if N==2:
        if A[0]==A[1]:
            return 'Second'
        else:
            return 'First'

    if N%2==0:#後手で最後
        C=Counter(A)
        if all([x%2==0 for x in C.values()]):
            return 'Second'
        
        return 'First'
    else:
        return 'Second'
    

def main():
    import sys
    T=int(sys.stdin.readline())
    for _ in range(T):
        N=int(sys.stdin.readline())
        A=list(map(int,sys.stdin.readline().split()))
        print(solve(N,A))
main()