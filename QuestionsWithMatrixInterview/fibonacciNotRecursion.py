def fibo(n):
    f = [1]*(n+1)
    for i in range(2,n+1):
        f[i] = f[i-1]+f[i-2]
    
    return f[n]

print(fibo(10))