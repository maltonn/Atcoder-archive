def main():
    import sys
    N=int(sys.stdin.readline())
    T=sys.stdin.readline().strip()
    if len(T)<=3:
        if T in ['110','11','10','0']:
            print(10**10)
            return
        elif T=='01':
            print(10**10-1)
            return
        elif T=='1':
            print(2*10**10)
            return
        

    if T[:3]=='110':#110110
        start=0
    elif T[:3]=='011':#(11)0110110
        start=1
    elif T[:3]=='101':#(1)10110110
        start=2
    else:
        print(0)
        return

    if T[-3:]=='110':
        end=-1
    elif T[-3:]=='011':#11011(0)
        end=-3
    elif T[-3:]=='101':#1101(10)
        end=-2
    else:
        print(0)
        return

    TM=T[start:len(T)+end+1]
    count=TM.count('110')
    if len(TM)%3!=0 or count!=len(TM)//3:
        print(0)
        return

    k=0
    if start:
        k+=1
    if end!=-1:
        k+=1
    
    res=10**10-k-count+1
    print(res)



if __name__=='__main__':
    main()