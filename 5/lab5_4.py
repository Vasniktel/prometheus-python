def file_search(folder, filename):
	location = folder[0] + '/'
	
	for place in folder:
		if isinstance(place, list):
			tmp = file_search(place, filename)
			if tmp:
				location += tmp
				return location
		
		elif place == filename:
			location += place if place != folder[0] else ''
			return location
	
	return False

print(file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt'))
print(file_search(['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me'))
print(file_search(['/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py'))