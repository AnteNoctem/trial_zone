def phi(n):
    
    t = []
    t2 = []
    k = 0
    a = 0
    
    if n <= 0:
        return 'n/a'
    
    #поиск простых чисел меньше n
    #решето Эратосфена
    for i in range(2, n+1):
        t += [i]
    for i in t:
        while a < len(t):
            if (t[a] % i == 0) and (t[a] != 2):
                b = t[a]
                t2 += [b]
            a += 1
        a = 1 + i
    c = list(set(t2))
    c2 = [i for i in t if i not in c]
    
    if (n == 1) or (n == 2):
        return 1
    elif n == c2[-1]:
        return n - 1
    
    #представить n в виде произведения простых чисел
    te = []
    n2 = n
    cnt = []
    for i in range(len(c2)):
        cn = 0
        while n2 % c2[i] == 0:
            n2 //= c2[i]
            te += [c2[i]]
            cn += 1
        if cn != 0:
            cnt += [cn]
    te = list(set(te))
    te = sorted(te)
    
    x = 1
    for i in range(len(te)):
        x *= te[i] ** cnt[i] - te[i] ** (cnt[i] -1)
    return x
