import sys

s = sys.argv[1].replace(' ', '')

tmp = s.replace('()', '')
while s != tmp:
	s = tmp
	tmp = s.replace('()', '')

print('YES' if not len(s) else 'NO')