import sys

string = sys.argv[1].lower().replace(' ', '')

print('YES' if string == string[::-1] else 'NO')