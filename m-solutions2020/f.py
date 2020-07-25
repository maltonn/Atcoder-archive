def main():#WA
    from collections import defaultdict
    from bisect import bisect_left
    import sys
    N=int(sys.stdin.readline())
    x_dic={
        'U':defaultdict(list),
        'R':defaultdict(list),
        'D':defaultdict(list),
        'L':defaultdict(list),
    }
    y_dic={
        'U':defaultdict(list),
        'R':defaultdict(list),
        'D':defaultdict(list),
        'L':defaultdict(list),
    }

    XpY=defaultdict(lambda : defaultdict(list))
    XmY=defaultdict(lambda : defaultdict(list))

    for i in range(N):
        X,Y,U=sys.stdin.readline().split()
        X=int(X)
        Y=int(Y)
        x_dic[U][X].append(Y)
        y_dic[U][Y].append(X)
        
        XpY[X+Y][U].append(X)
        XmY[X-Y][U].append(X)

    mn=10**15

    for key,lst1 in x_dic['R'].items():
        if key in x_dic['L']:
            lst2=x_dic['L'][key]
            
            lst1.sort()
            lst2.sort()

            c1=0
            c2=0
            while True:
                if lst1[c1]<lst2[c2]:
                    tmp=(lst2[c2]-lst1[c1])*5
                    mn=tmp if tmp<mn else mn
                    c1+=1
                    if c1==len(lst1):
                        break
                else:
                    c2+=1
                    if c2==len(lst2):
                        break

            
    for key,lst1 in x_dic['U'].items():
        if key in x_dic['D']:
            lst2=x_dic['D'][key]
            
            lst1.sort()
            lst2.sort()

            c1=0
            c2=0
            while True:
                if lst1[c1]<lst2[c2]:
                    tmp=(lst2[c2]-lst1[c1])*5
                    mn=tmp if tmp<mn else mn
                    c1+=1
                    if c1==len(lst1):
                        break
                else:
                    c2+=1
                    if c2==len(lst2):
                        break

    for _,dic in XpY.items():
        if ('U' in dic and 'R' in dic):
            lst1=sorted(dic['R'])
            lst2=sorted(dic['U'])

            c1=0
            c2=0
            while True:
                if lst1[c1]<lst2[c2]:
                    tmp=(lst2[c2]-lst1[c1])*10
                    mn=tmp if tmp<mn else mn
                    c1+=1
                    if c1==len(lst1):
                        break
                else:
                    c2+=1
                    if c2==len(lst2):
                        break



        elif ('D' in dic and 'L' in dic):
            lst1=sorted(dic['D'])
            lst2=sorted(dic['L'])

            c1=0
            c2=0
            while True:
                if lst1[c1]<lst2[c2]:
                    tmp=(lst2[c2]-lst1[c1])*10
                    mn=tmp if tmp<mn else mn
                    c1+=1
                    if c1==len(lst1):
                        break
                else:
                    c2+=1
                    if c2==len(lst2):
                        break

    for _,dic in XmY.items():
        if ('U' in dic and 'L' in dic):
            lst1=sorted(dic['U'])
            lst2=sorted(dic['L'])

            c1=0
            c2=0
            while True:
                if lst1[c1]<lst2[c2]:
                    tmp=(lst2[c2]-lst1[c1])*10
                    mn=tmp if tmp<mn else mn
                    c1+=1
                    if c1==len(lst1):
                        break
                else:
                    c2+=1
                    if c2==len(lst2):
                        break



        elif ('D' in dic and 'R' in dic):
            lst1=sorted(dic['R'])
            lst2=sorted(dic['D'])

            c1=0
            c2=0
            while True:
                if lst1[c1]<lst2[c2]:
                    tmp=(lst2[c2]-lst1[c1])*10
                    mn=tmp if tmp<mn else mn
                    c1+=1
                    if c1==len(lst1):
                        break
                else:
                    c2+=1
                    if c2==len(lst2):
                        break

    if mn==10**15:
        print('SAFE')
    else:
        print(mn)

main()
