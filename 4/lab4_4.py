import sys

arg_1 = sys.argv[1]
arg_2 = sys.argv[2]
count = 0

for i in xrange(int(arg_1), int(arg_2) + 1):
	str_ = str(i)
	
	if len(str_) < 6:
		str_ = '0' * (6 - len(str_)) + str_
	
	int_1 = int_2 = 0
	
	for j in range(6):
		if j < 3:
			int_1 += int(str_[j])
		else:
			int_2 += int(str_[j])
	
	if int_1 == int_2:
		count += 1

print(count)