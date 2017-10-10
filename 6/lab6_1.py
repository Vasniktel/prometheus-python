def count_holes(n):
	if not (isinstance(n, (int, long)) or (isinstance(n, str) and len(n) and ((n[0] == '-' and n[1:].isdigit()) or n.isdigit()))):
		return 'ERROR'
	
	n = str(abs(int(n)))
	count = 0
	
	for e in n:
		if e in ['0', '4', '6', '9']:
			count += 1
		elif e == '8':
			count += 2
	
	return count


print count_holes('123'), '0'
print count_holes(906), '3'
print count_holes('001'), '0'
print count_holes(-8), "2"
print count_holes(-8.0), "ERROR"
print '---'
print count_holes(0), "1"
print count_holes(888888888888888888888), "42"
print count_holes(-888888888888888888888), "42"
print count_holes(69L), "2"
print count_holes('000000000010'), "1" 
print count_holes('888888888888888888888.0'), "ERROR"
print count_holes(''), "ERROR"
print count_holes([1]), "ERROR"
print count_holes(None), "ERROR"
print count_holes('qq'), "ERROR"
