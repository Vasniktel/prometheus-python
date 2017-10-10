import re

def find_most_frequent(text):
	if text == '':
		return []
	
	text_list = re.sub('[,.:;!?\-]+', ' ', text.lower()).split()
	
	if text_list == []:
		return []
	
	occurrences = dict([(el, text_list.count(el)) for el in text_list])
	
	max_val = max(occurrences, key = lambda i: occurrences[i])
	
	return sorted([key for key in occurrences.keys() if occurrences[key] == occurrences[max_val]])


print(find_most_frequent('Hello,Hello, my dear!'))
print(find_most_frequent('to understand recursion you need first to understand recursion...'))
print(find_most_frequent('Mom! Mom! Are you sleeping?!!!'))