from fractions import gcd

def find_fraction(summ):
	if isinstance(summ, (int, long)) and summ > 0:
		for i in range(summ // 2, 0, -1):
			if i != summ - i and gcd(i, summ - i) == 1:
				return (i, summ - i)
	
	return False


print(find_fraction(2)) # False
print(find_fraction(3)) # (1, 2)
print(find_fraction(10)) # (3, 7)
print(find_fraction(62)) # (29, 33)
print(find_fraction(150000001)) # (75000000, 75000001)