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

print(clean_list([1, 1.0, '1', -1, 1]))
print(clean_list(['qwe', 'reg', 'qwe', 'REG']))
print(clean_list([32, 32.1, 32.0, -123]))
print(clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]))