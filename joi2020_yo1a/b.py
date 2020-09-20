from collections import Counter
s='s'

def p(x):
    if type(x)==list:
        print(' '.join(x))
    else:
        print(x)
    
def YN(bl,_true='Yes',_false='No'):
    if bl:
        print(_true)
    else:
        print(_false)

def main1():
    if True:
        t=1
        k=0
        import sys
        inputs=list(sys.stdin)

        for j,line in enumerate(inputs):
            if j==0:
                L=list(map(int,line.split()))
                L1=list(map(int,line.split()))
            elif j==1:
                L2=list(map(int,line.split()))
            elif j==2:
                L3=list(map(int,line.split()))

            L=list(map(int,line.split()))
            LC=Counter(L)
            for i,a in enumerate(L):
                try:
                    if j==0:
                        a1=L[0]
                        b1=L[1]
                        c1=L[2]
                        d1=L[3]
                        e1=L[4]
                        a=L[0]
                        b=L[1]
                        c=L[2]
                        d=L[3]
                        e=L[4]
                    elif j==1:
                        a2=L[0]
                        b2=L[1]
                        c2=L[2]
                        d2=L[3]
                        e2=L[4]
                    elif j==2:
                        a3=L[0]
                        b3=L[1]
                        c3=L[2]
                        d3=L[3]
                        e3=L[4]
                except:
                    pass
    
    

def main2():
    if True:
        k=0
        t=1
        F=list(map(int,input().split()))
        try:
            N=F[0]
            M=F[1]
            K=F[2]
        except:
            pass

        L=[]
        L1=[]
        L2=[]
        L3=[]
        for i in range(N):
            IL=list(map(int,input().split()))
            try:
                L.append(IL[0])
                L1.aooebd(IL[0])
                L2.append(IL[1])
                L3.append(IL[2])
            except:
                pass

    

def main3():
    if True:
        import sys
        L=[]
        L1=[]
        L2=[]
        L3=[]
        inputs=list(sys.stdin)
        for line in inputs:
            try:
                IL=list(map(int,line.split()))
                L.append(IL[0])
                L1.append(IL[0])
                L2.append(IL[1])
                L3.append(IL[2])
            except:
                pass

    


def main_s():
    if True:
        from collections import Counter
        t=1
        k=0
        import sys
        inputs=list(sys.stdin)

        for j,line in enumerate(inputs):
            s=line
            if j==0:
                rs=reversed(s)
                sc=Counter(s)
                sl=list(s)
                
                s1=s
                rs1=reversed(s)
                sc1=Counter(s)
                sl1=list(s)
                
            elif j==1:
                s2=s
                rs2=reversed(s)
                sc2=Counter(s)
                sl2=list(s)
            elif j==2:
                s3=s
                rs3=reversed(s)
                sc3=Counter(s)
                sl3=list(s)
            
    


def main():
    pass




mode=s







if mode==1:
    main1()
elif mode==2:
    main2()
elif mode==3:
    main3()
elif mode=='s':
    main_s()
else:
    main()




