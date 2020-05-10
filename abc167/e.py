

class CMB():
    def __init__(self, mod=10**9+7,mx=2*10**5):#mx:入力制限
        N = mx
        g1 = [1, 1]  # 元テーブル
        g2 = [1, 1]  # 逆元テーブル
        inverse = [0, 1]  # 逆元テーブル計算用テーブル
        for i in range(2, N + 1):
            g1.append((g1[-1] * i) % mod)
            inverse.append((-inverse[mod % i] * (mod//i)) % mod)
            g2.append((g2[-1] * inverse[-1]) % mod)
        self.g1 = g1
        self.g2 = g2
        self.mod = mod

    def cmb(self, n, r):  # 素数で割って出力　の場合
        if r==0:
            return 1
        if (r < 0 or r > n):
            return 0
        r = min(r, n-r)
        return self.g1[n] * self.g2[r] * self.g2[n-r] % self.mod


def main():
    C=CMB(mod=998244353,mx=2*10**5)
    def H(n, r):
        
        return CMB.cmb(n+r-1, r, 998244353)
    
    import sys
    N,M,K=list(map(int,sys.stdin.readline().split()))
    out=0
    for i in range(K+1):
        out+=C.cmb(M,N-i)*H(N,i)
        out%=998244353
    print(out)
main()