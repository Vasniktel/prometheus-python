import sys

args = sys.argv[1:][::-1]
out = args[0]

for arg in args[1:]:
	out += ' ' + arg

print(out)