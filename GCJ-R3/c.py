def solve():
    def Case_1():
        Asd=set(A)
        for a in Asd:
            if a%2==0 and a//2 in Asd:
                return 1

        return 2



    from collections import Counter
    N,D=map(int,input().split())
    A=list(map(int,input().split()))
    t=360*10**9-sum(A)
    if t:
        A.append(t)
    A.sort()

    C=Counter(A)
    mx=max(C.values())
    if mx>=D:
        return 0
    elif mx==1 and D==3:
        return Case_1()
    elif mx==1 and D==2:
        return 1
    elif mx==2:
        C_2={key:val for key,val in C.items() if val==2}
        piece_size=sorted(C_2.items(),key=lambda x: x[0])[0][0]
        if piece_size!=A[-1]:
            return 1
        else:
            return Case_1()


    else:
        return 'IMPOSSIBLE'


    

def main():
    T=int(input())
    for case in range(1,T+1):
         print('Case #{}: {}'.format(case,solve()))

main()