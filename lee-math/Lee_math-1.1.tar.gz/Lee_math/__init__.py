#Lee的数学库--始建于2021.9
def gcd(a,b):                              #辗转相除法求最大公因数
    while b != 0:
        a,b = b,a%b
    return a


def prime_pi(n):
    count=3         #找出n以内的所有素数（所有大于三的素数只有6N-1,和6N+1两种形式）
    x=7
    step =4
    prime_number=[2,3,5]
    while x< n:
        if x%5!=0:
            edge=int(x**0.5)+1
            for i in range(3,edge,2):
                if x %i ==0:
                    break
            else:
                count+=1
                prime_number.append(x)
        x+=step
        step=4 if step==2 else 2
    return(prime_number)


def mimo(a,b,c):   #大数模幂运算
    a=a%c
    ans=1
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1#移位
        a=(a*a)%c
    return ans


def is_prime(n):#素性检测
    import random
    K =100
    k = 0
    while(k<K):
        flag = False
        while(not flag):
            b = int(random.random()*(n-2))
            if(b>=2 and b<=n-2):
                flag = 5
        factor = gcd(b,n)#计算(b,n)
        r = mimo(b,n-1,n) #计算b^(n-1)modn
        if(factor >1):
            return 0
            break
        elif(r!=1):
            return 0
            break
        else:
            k+=1
    if(k==K):
        return 1
    else:
        return 0




def CRT(a_list, m_list):#中国剩余定理
    def Get_Mi(m_list, M):  # 获取所有的Mi
        M_list = []
        for mi in m_list:
            M_list.append(M // mi)
        return M_list

    def Get_ei_list(M_list, m_list):  # 取所有的Mi的逆元
        ei_list = []
        for i in range(len(M_list)):
            ei_list.append(Get_ei(M_list[i], m_list[i])[0])
        return ei_list

    def Get_ei(a, b):
        # 计算ei

        if 0 == b:
            x = 1
            y = 0
            q = a
            return x, y, q
        xyq = Get_ei(b, a % b)
        x = xyq[0]
        y = xyq[1]
        q = xyq[2]
        temp = x
        x = y
        y = temp - a // b * y
        return x, y, q

    # 计算中国剩余定理，返回计算结果
    M = 1  # M是所有mi的乘积
    for mi in m_list:
        M *= mi
    Mi_list = Get_Mi(m_list, M)
    Mi_inverse = Get_ei_list(Mi_list, m_list)
    x = 0
    for i in range(len(a_list)):  # 开始计算x
        x += Mi_list[i] * Mi_inverse[i] * a_list[i]
        x %= M
    return x


def array_sim():#化简矩阵
    import numpy as np
    from sympy import Matrix
    a11 = eval(input('a11:'))
    a12 = eval(input('a12:'))
    a13 = eval(input('a13:'))
    a14 = eval(input('a14:'))
    a15 = eval(input('a15:'))
    a21 = eval(input('a21:'))
    a22 = eval(input('a22:'))
    a23 = eval(input('a23:'))
    a24 = eval(input('a24:'))
    a25 = eval(input('a25:'))
    a31 = eval(input('a31:'))
    a32 = eval(input('a32:'))
    a33 = eval(input('a33:'))
    a34 = eval(input('a34:'))
    a35 = eval(input('a35:'))
    a41 = eval(input('a41:'))
    a42 = eval(input('a42:'))
    a43 = eval(input('a43:'))
    a44 = eval(input('a44:'))
    a45 = eval(input('a45:'))
    matrix = [
        [a11, a12, a13, a14, a15],
        [a21, a22, a23, a24, a25],
        [a31, a32, a33, a34, a35],
        [a41, a42, a43, a44, a45],
    ]
    rref = Matrix(np.array(matrix)).rref()[0].tolist()
    return rref


def dlog(p,g,h):#求离散对数
    def mimo(a, b, c):  # 大数模幂运算
        a = a % c
        ans = 1
        while b != 0:
            if b & 1:
                ans = (ans * a) % c
            b >>= 1  # 移位
            a = (a * a) % c
        return ans

    import math
    m=int(math.sqrt(p))
    lis=[]
    q=0
    for r in range(m):
        a= (mimo(h, 1, p) * mimo(g, r, p)) % p
        lis.append(a)
    for k in range(1,math.ceil(m)+1):
        g_=mimo(g, k * m, p)
        for i in range(len(lis)):
            if g_==lis[i]:
                q=k
                r=i
                break
    x=q*m-r
    return x


def weida (add,muliply):#韦达定理
    import math
    if pow(add, 2) - 4 * muliply <0:
        return [0,0]
    else:
        deta=math.sqrt(pow(add,2)-4*muliply)
        x1=1/2*(add-deta)
        x2=1/2*(add+deta)
        return [x1,x2]


def lianfenshu(a,b,n):#计算连分数（分子，分母，循环次数，默认为10次），返回【简单连分数，pi，qi】
    import decimal
    jingdu = n+10
    jingdu = int(jingdu)
    decimal.getcontext().prec = jingdu
    x = [decimal.Decimal(a) / decimal.Decimal(b)]
    k = []  # 渐进连分数分子
    d = []  # 渐进连分数分母
    a = []  # 简单连分数列表
    for i in range(n):  # 一百次循环，再高精度会丢失
        tem = int(x[i])
        a.append(tem)
        if i == 0:
            fenzi = a[i]
            fenmu = 1
            k.append(fenzi)
            d.append(fenmu)
        if i == 1:
            fenzi = a[i] * a[i - 1] + 1
            fenmu = a[i]
            k.append(fenzi)
            d.append(fenmu)
        if i >= 2:
            # temp1=k[i-1]*a[i]
            fenzi = k[i - 1] * a[i] + k[i - 2]
            # temp2=d[i-1]*a[i]
            fenmu = d[i - 1] * a[i] + d[i - 2]
            k.append(fenzi)
            d.append(fenmu)
        if x[i] == tem:
            break
        x.append(decimal.Decimal(str(1)) / (decimal.Decimal(str(x[i])) - decimal.Decimal(str(tem))))
    return [a,k,d]
