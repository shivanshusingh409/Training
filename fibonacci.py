def fibonacci(n):
  fibonacci_series=[]
  a, b=0,1
  for _ in range(n):
    fibonacci_series.append(a)
    a, b = b, a+b
  return fibonacci_series

n=20
series=fibonacci(n)
print(series)
