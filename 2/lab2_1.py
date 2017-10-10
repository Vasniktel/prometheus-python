import sys
import math

x = float(sys.argv[1])
u = float(sys.argv[2])
o = float(sys.argv[3])

f = math.exp(-(x - u) ** 2 / (2 * o ** 2)) / (o * math.sqrt(2 * math.pi))
print(f)