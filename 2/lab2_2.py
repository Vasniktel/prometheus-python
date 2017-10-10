import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

song = 'Everybody sing a song:'
word = 'la'
ending = '!' if z == 1 else '.'

for i in range(x - 1):
	word += '-la'

print(song + (' ' + word) * y + ending)