from time import time

def bouquets(narcissus_price, tulip_price, rose_price, summ):
	count = 0
	args = sorted([narcissus_price, tulip_price, rose_price])
	amounts = {
		'cheap': [None, args[0]],
		'medium': [None, args[1]],
		'expensive': [None, args[2]]
	}
	del args
	
	for i in range(1, int(summ // amounts['cheap'][1] + 1), 2):
		amounts['cheap'][0] = i
		amounts['medium'][0] = 0
		amounts['expensive'][0] = 0
		
		for j in range(int((i + 2) / 2.0 * (i + 1))):
			cost = amounts['cheap'][0] * amounts['cheap'][1] + amounts['medium'][0] * amounts['medium'][1] + amounts['expensive'][0] * amounts['expensive'][1]
			
			if cost <= summ:
				count += 1
			elif not (amounts['expensive'][0] and amounts['cheap'][0]):
				break
			else:
				amounts['medium'][0] += amounts['expensive'][0] + 1
				amounts['expensive'][0] = 0
				amounts['cheap'][0] -= 1
				continue
			
			if amounts['medium'][0]:
				amounts['medium'][0] -= 1
				amounts['expensive'][0] += 1
			elif amounts['cheap'][0]:
				amounts['medium'][0] = amounts['expensive'][0] + 1
				amounts['expensive'][0] = 0
				amounts['cheap'][0] -= 1
	
	return count


while True:
	try:
		num1 = float(input('Num1: '))
		num2 = float(input('Num2: '))
		num3 = float(input('Num3: '))
		num4 = float(input('Num4: '))
		start = time()
		print(bouquets(num1, num2, num3, num4))
		print(time() - start)
	except ValueError:
		break