def call(n):
    print(n)
    if n ==1:
        return n
    elif n%2==0:
        return call(n//2)
    else:
        return call(3*n + 1)
call(10)
