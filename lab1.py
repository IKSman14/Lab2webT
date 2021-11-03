def palind(Chis):
    Spis = list(str(Chis))
    Dlin = len(Spis)
    for i in range(Dlin//2 - 1):
        if (Chis - (Chis % (10 ^ (Dlin - i - 1)))) / (10 ^ (Dlin - i - 1)) == Chis % 10:
            Chis = (Chis % (10 ^ (Dlin-i-1))) // 10
            continue
        else:
            print(Chis, " не палиндром")
            return False
    print(Chis, "палиндром")

def sotr (IntSp):
    Two = list()
    Three = list()
    Four = list()
    for i in IntSp:
        if i % 2 == 0:
            Two.append(i)
            if i % 4 == 0:
                Four.append(i)
        if i % 3 == 0:
            Three.append(i)
    return Two, Three, Four

def revers(A):
    res = 0
    Out = A
    Long = len(list(str(A)))
    if A < 0:
        Long = Long - 1
    for i in range(Long):
        res += ((A % 10) * (pow(10, (Long - i - 1))))
        A = A // 10
    if A < 0:
        res *= -1
    print(res, " - обратное чило для", Out)

def rootNewt(a, n :int, acc :float):
    Now = a / n - 1
    while abs(Now ** n - a) > acc:
        Now = 1 / n * ((n - 1) * Now + a / (Now ** (n - 1)))
    print(f"{a}^(1/{n}) = {Now}")

def checkSimple(n: int):
    if n < 2:
        print(f"{n} - не простое число")
        return False
    if n == 2:
        print(f"{n} - простое число")
        return True
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            print(f"{n} - не простое число")
            return False
    print(f"{n} - простое число")


palind(123321)
print(sotr([1, 2, 4, 10, 15]))
revers(1450)
rootNewt(999, 5, 0.000001)
checkSimple(129)


