def main():
    import math
    pi=math.pi
    import sys
    A,B,H,M=list(map(int,sys.stdin.readline().split()))

    large_deg=((2*pi/12)*((H+M/60)%12))
    small_deg=((2*pi/60)*(M%60))

    deg=abs(large_deg-small_deg)

    if deg>=pi:
        deg=2*pi-deg
    print(math.sqrt(A**2+B**2-2*A*B*math.cos(deg)))
    

main()
