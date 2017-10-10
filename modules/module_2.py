convert_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert_n_to_m(x, n, m):
	if not is_num_valid(x, n):
		return False
	
	if n == m:
		return str(x)
	
	dec = 0
	result = ''
	
	if n == 10:
		dec = int(x)
	else:
		x = str(x).upper()[::-1]
		
		if n == 1:
			dec = x.count('0')
		else:
			for i in range(len(x)):
				dec += convert_str.index(x[i]) * n ** i
	
	if dec == 0:
		return '0'
	
	if m == 1:
		return '0' * dec
	
	while dec:
		result += convert_str[dec % m]
		dec //= m
	
	return result[::-1]
	

def is_num_valid(x, n):
	if not isinstance(x, (int, str, long)):
		return False
	
	x = str(x).upper()
	
	if x.find('-') != -1 or x.find('.') != -1:
		return False
	
	error_list = [i for i in convert_str[n:] if x.find(i) != -1] + [i for i in x if convert_str.find(i) == -1]
	
	if len(error_list):
		return False
	
	return True



def test():
    print(1,convert_n_to_m([1], 2, 2) == False) # 1
 
    print(2,convert_n_to_m([1], 2, 2) == False) # 2
 
    print(3,convert_n_to_m({1: 0}, 2, 2) == False) # 3
 
    print(4,convert_n_to_m(123123123123123123123.0, 11, 16) == False) # 4
 
    print(5,convert_n_to_m(100, 2, 1) == '0000') # 5
 
    print(6,convert_n_to_m(0, 10, 2)  == '0') # 6
 
    print(7,convert_n_to_m(000, 10, 2)   == '0') # 7
 
    print(8,convert_n_to_m(777, 10, 2)  == '1100001001') # 8
 
    print(9,convert_n_to_m(777L, 10, 2)   == '1100001001') # 9
 
    print(10,convert_n_to_m('000', 10, 2)   == '0') # 10
 
    print(11,convert_n_to_m('ZZZZ', 36, 13)   == '46A672') # 11
 
    print(12,convert_n_to_m('000ZZZZ', 36, 13)   == '46A672') # 12
 
    print(13,convert_n_to_m('ZZZZ', 35, 13)   == False) # 13
 
    print(14,convert_n_to_m('qweasd', 33, 36)  == 'HGPEYJ') # 14
 
    print(15,convert_n_to_m('123123123123123123123', 11, 16)   == '2C09BC518E8048D23A') # 15
 
    print(16,convert_n_to_m(123123123123123123123, 11, 16)    == '2C09BC518E8048D23A') # 16
 
    print(17,convert_n_to_m(123123123123123123123, 10, 10)     == '123123123123123123123') # 17
 
    print(18,convert_n_to_m('bnh34521', 31, 14)     == '119337DC2BC') # 18
 
    print(19,convert_n_to_m('bnh34521', 11, 14)    == False) # 19
 
test()