import sys


key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_str = sys.argv[1].replace(' ', '')
str_arr = []
result = ''


start = 0
end = 5
for i in range(len(input_str) // 5):
	str_arr.append(input_str[start:end])
	start += 5
	end += 5


if len(str_arr[-1]) < 5:
	del str_arr[-1]


for s in str_arr:
	code = ''
	for c in s:
		if c.islower():
			code += 'a'
		else:
			code += 'b'
	
	result += alphabet[key.find(code)]

print(result)