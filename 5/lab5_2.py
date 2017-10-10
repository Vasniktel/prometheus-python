def counter(a, b):
	a = str(a)
	b = clean_list(str(b))
	counter = 0
	
	for e in b:
		if is_in_list(a, e):
			counter += 1
	
	return counter

def clean_list(list_to_clean):
	return_list = []
	
	for e in list_to_clean:
		if not is_in_list(return_list, e):
			return_list.append(e)
	
	return return_list

def is_in_list(list_to_find, val):
	for e in list_to_find:
		if isinstance(e, type(val)) and e == val:
			return True
	
	return False

print(counter(12345, 567))
print(counter(1233211, 12128))
print(counter(123, 45))