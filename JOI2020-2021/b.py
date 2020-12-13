import sys


def solve1(lst):
    res=0
    while True:
        tmp=[]
        now=0
        for a in lst:
            if a!=now:
                tmp.append(a)
                now=a
        lst=tmp.copy()

        if lst[0] in lst[1:]:
            res+=1
            k=len(lst)-2-lst[len(lst):0:-1].index(lst[0])
            for i in range(k):
                if i>k-i:
                    break
                lst[i],lst[k-i]=lst[k-i],lst[i]

        else:
            if len(lst)<=3:
                if lst==sorted(lst):
                    return res
                else:
                    if len(lst)==2:
                        return res+1
                    elif lst==[3,1,2] or lst==[1,3,2] or lst==[2,3,1]:
                        return res+2
                    else:
                        return res+1

            else:
                if lst[1] in lst[2:]:
                    lst[0],lst[1]=lst[1],lst[0]
                    res+=1
                else:
                    1/0#err

def solve2(lst):
    res=0
    while True:
        now=0   
        tmp=[]
        for a in lst:
            if a!=now:
                tmp.append(a)
                now=a
        lst=tmp.copy()

        if lst[0] in lst[1:]:
            res+=1
            k=len(lst)-2-lst[len(lst):0:-1].index(lst[0])
            for i in range(k):
                if i>k-i:
                    break
                lst[i],lst[k-i]=lst[k-i],lst[i]


        else:
            if len(lst)<=3:
                if lst==sorted(lst):
                    return res
                else:
                    if len(lst)==2:
                        return res+1
                    elif lst==[3,1,2] or lst==[1,3,2] or lst==[2,3,1]:
                        return res+2
                    else:
                        return res+1

            else:
                lst=list(reversed(lst))
                res+=1


           

def solve3(lst):
    res=0
    while True:
        tmp=[]
        now=0
        for a in lst:
            if a!=now:
                tmp.append(a)
                now=a
        lst=tmp.copy()

        if lst[0] in lst[1:]:
            res+=1
            k=lst[1:].index(lst[0])
            for i in range(k):
                if i>k-i:
                    break
                lst[i],lst[k-i]=lst[k-i],lst[i]

        else:
            if len(lst)<=3:
                if lst==sorted(lst):
                    return res
                else:
                    if len(lst)==2:
                        return res+1
                    elif lst==[3,1,2] or lst==[1,3,2] or lst==[2,3,1]:
                        return res+2
                    else:
                        return res+1

            else:
                if lst[1] in lst[2:]:
                    lst[0],lst[1]=lst[1],lst[0]
                    res+=1
                else:
                    1/0#err

def solve4(lst):
    res=0
    while True:
        now=0   
        tmp=[]
        for a in lst:
            if a!=now:
                tmp.append(a)
                now=a
        lst=tmp.copy()

        if lst[0] in lst[1:]:
            res+=1
            k=lst[1:].index(lst[0])
            for i in range(k):
                if i>k-i:
                    break
                lst[i],lst[k-i]=lst[k-i],lst[i]


        else:
            if len(lst)<=3:
                if lst==sorted(lst):
                    return res
                else:
                    if len(lst)==2:
                        return res+1
                    elif lst==[3,1,2] or lst==[1,3,2] or lst==[2,3,1]:
                        return res+2
                    else:
                        return res+1

            else:
                lst=list(reversed(lst))
                res+=1



def main():
    import sys
    dic={
        'A':1,
        'B':2,
        'C':3,
    }
    N,Q=list(map(int,sys.stdin.readline().split()))
    for i in range(Q):
        lst=[dic[x] for x in sys.stdin.readline().strip()]
        a=solve1(lst.copy())
        b=solve2(lst.copy())
        c=solve1(list(reversed(lst)).copy())
        d=solve2(list(reversed(lst)).copy())

        e=solve3(lst.copy())
        f=solve4(lst.copy())
        g=solve3(list(reversed(lst)).copy())
        h=solve4(list(reversed(lst)).copy())
        print(min(a,b,c+1,c+1,e,f,g+1,h+1))

    


if __name__=='__main__':
    main()