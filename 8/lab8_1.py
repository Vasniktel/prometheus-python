class CombStr(object):
	def __init__(self, string):
		self.string = string
	
	def count_substrings(self, length):
		if not length or length > len(self.string):
			return 0
		
		found = []
		
		for i in range(len(self.string)):
			substr = self.string[i:length + i]
			if len(substr) != length:
				break
			if substr not in found:
				found.append(substr)
		
		return len(found)


s0 = CombStr('qqqqqqweqqq%')
print(s0.count_substrings(0)) # 0
print(s0.count_substrings(1)) # 4
print(s0.count_substrings(2)) # 5
print(s0.count_substrings(5)) # 7
print(s0.count_substrings(15)) # 0