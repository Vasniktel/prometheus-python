class SuperStr(str):
	def is_repeatance(self, string):
		if not isinstance(string, str) or self == '' or string == '':
			return False
		
		s = self
		found = s.find(string)
		
		while found != -1:
			s = s[found + len(string):]
			found = s.find(string)
		
		if len(s):
			return False
		
		return True
	
	def is_palindrom(self):
		s = self.lower()
		return s == s[::-1]




s1 = SuperStr('678678678678')
print(s1.is_repeatance('6786')== False)
print(s1.is_repeatance('678')== True)
print(s1.is_repeatance('678678')== True)
print(s1.is_repeatance('678678678')== False)
print(s1.is_repeatance('q')== False)
print(s1.is_repeatance('')== False)
print(s1.is_repeatance(678)== False)
print(s1.is_repeatance([])== False)
print(s1.is_repeatance([678])== False)
print(s1.is_palindrom()== False)
print(s1.isdigit()== True)
print(int(s1)== 678678678678)
print('("' + s1 + '")'== '("678678678678")')
s2 = SuperStr('')
print(s2.is_repeatance('')== False)
print(s2.is_repeatance('a')== False)
print(s2.is_palindrom()== True)
print(bool(s2)== False)
s3 = SuperStr('mystring1Gnirtsym')
print(s3.is_repeatance('my')== False)
print(s3.is_repeatance('q,.%;#')== False)
print(s3.is_palindrom()== True)
print(s3.lower()== 'mystring1gnirtsym')
print(s3== 'mystring1Gnirtsym')
s4 = SuperStr('q')
print(s4.is_repeatance('')== False)
print(s4.is_repeatance('q')== True)
print(s4.is_palindrom()== True)
print(s4.upper()== 'Q')