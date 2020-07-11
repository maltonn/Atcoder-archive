def main():
    import sys
    N=int(sys.stdin.readline())
    X=sys.stdin.readline()

    no=X.count('1')
    np=no+1
    nm=no-1
    nm_flag=bool(nm)

    np_mods=[-1]*N
    nm_mods=[-1]*N
    
    np_mods[0]=1
    nm_mods[0]=1
    
    for i in range(1,N):
        np_mods[i]=(np_mods[i-1]*2)%np
        if nm_flag:
            nm_mods[i]=(nm_mods[i-1]*2)%nm

    np_mods.reverse()
    nm_mods.reverse()
    
    np_mods_sum=0
    nm_mods_sum=0
    for i in range(N):
        if X[i]=='1':
            np_mods_sum+=np_mods[i]
            nm_mods_sum+=nm_mods[i]

    for i in range(N):
        if X[i]=='0':
            n=(np_mods_sum+np_mods[i])%np

        else:
            if nm_flag:
                n=(nm_mods_sum-nm_mods[i])%nm
            else:
                print(0)
                continue
        if n==0:
            print(1)
            continue
        count=1
        while True:
            bs=str(bin(n))[2:]
            k=bs.count('1')
            n=n%k
            count+=1
            if n==0:
                break
        print(count)

main()