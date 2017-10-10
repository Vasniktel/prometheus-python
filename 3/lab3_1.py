import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

msg = 'triangle' if a + b > c and a + c > b and b + c > a else 'not triangle'

print(msg)