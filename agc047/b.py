def main():#TLE
    import sys
    N=int(input())
    L=['']*N
    for i in range(N):
        L[i]=''.join(reversed(list(input())))
    
    L.sort()

    count=0
    for i in range(N):
        k=1
        while True:
            if i+k>=N:
                break

            if L[i][:-1]==L[i+k][:len(L[i])-1]:
                if L[i][-1] in L[i+k][len(L[i])-1:]:
                    count+=1
                k+=1
            else:
                break


        k=1
        while True:
            if i-k==-1:
                break
            if L[i][:-1]==L[i-k][:len(L[i])-1]:
                if L[i][-1] in L[i-k][len(L[i])-1:]:
                    count+=1
                k+=1
            else:
                break

    print(count)

main()
