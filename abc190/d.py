def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def main():
    import sys
    N=int(sys.stdin.readline())
    st=set()
    N*=2

    lst=factorization(N)
    def dfs(i,num):
        if i==len(lst):
            a=num
            b=N//num

            if (a+b-1)%2==1:
                return
            else:
                e=(a+b-1)//2
                s=a-e
            if e<s:
                s,e=e,s
            
            st.add((s,e))
            return

        for j in range(lst[i][1]+1):
            dfs(i+1,num*pow(lst[i][0],j))

    dfs(0,1)
    print(len(st))

if __name__ == "__main__":
    main()