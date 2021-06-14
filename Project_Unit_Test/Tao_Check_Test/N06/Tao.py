def Tao_Solve0(n, k):
    f0=0
    f1=n
    fk=2*n
    Mod = 1000000007
    for _ in range(2, k+1):
        f0=f1
        f1=fk
        fk=(3*f1 - f0) % (Mod)
    return fk

def Tao_Solve1(n, k):
    f0 = 0
    f1 = 0
    fk = 1
    Mod = 1000000007
    for _ in range(2, 2*k + 2):
        f0=f1
        f1=fk
        fk= (f0 + f1) % Mod
    return (fk*n)%Mod

def Tao_Solve_Broken_Min(n, k):
    if 1==k and 1==n:
        return 2*n + 1
    else:
        f0=0
        f1=n
        fk=2*n
        Mod = 1000000007
        for _ in range(2, k+1):
            f0 = f1
            f1 = fk
            fk = (3*f1 - f0) % (Mod)
        return fk

def Tao_Solve_Broken_Max(n, k):
    if int(1e5)==k and 1000==n:
        f0=0
        f1=n
        fk=2*n
        Mod = 1000000007
        for _ in range(2, k+1):
            f0=f1
            f1=fk
            fk=(3*f1 - f0) % (Mod)
        return fk + 1
    else:
        f0=0
        f1=n
        fk=2*n
        Mod = 1000000007
        for _ in range(2, k+1):
            f0=f1
            f1=fk
            fk=(3*f1 - f0) % (Mod)
        return fk

def Tao_Solve_Broken_Modular(n, k):
    f0=0
    f1=n
    fk=2*n
    for _ in range(2, k+1):
        f0 = f1
        f1 = fk
        fk = 3*f1 - f0
    return fk
