def f(n):  
    r= 1  
    for i in range(2,n+1):  
        r *= i  
    return r  
while True:  
  n=int(input())  
  print(f(n))