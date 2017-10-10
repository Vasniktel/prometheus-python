def super_fibonacci(n, m):
	fib = [0] + [1 for i in range(m)]
	
	for i in range(m + 1, n + 1):
		val = 0
		for k in fib[i - m:i]:
			val += k
		
		fib.append(val)
	
	return fib[n]


print(super_fibonacci(2, 1))
print(super_fibonacci(3, 5))
print(super_fibonacci(8, 2))
print(super_fibonacci(9, 3))