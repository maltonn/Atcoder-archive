def main():
    import sys
    N=int(sys.stdin.readline())
    L=[0]*(10**4+1)
    for x in range(1,1000):
        for y in range(x,1000):
            for z in range(y,1000):
                r=x**2+y**2+z**2+x*y+y*z+z*x
                if r>10**4:
                    break
                
                c=len(set((x,y,z)))
                if c==3:
                    L[r]+=6
                elif c==2:
                    L[r]+=3
                elif c==1:
                    L[r]+=1


    for t in L[1:N+1]:
        print(t)

main()