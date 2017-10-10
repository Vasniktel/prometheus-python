from maze_runner import MazeRunner

def maze_controller(robot):
	steps = [[(0, 0), True, 'down']]
	direction = 'down'
	position = None
	
	def is_opposite(position):
		return (position[2] == 'up' and direction == 'down') or \
			(position[2] == 'down' and direction == 'up') or \
			(position[2] == 'left' and direction == 'right') or \
			(position[2] == 'right' and direction == 'left')
	
	def create_location(position):
		if direction == 'down':
			return {
				'left': ((position[0][0] + 1, position[0][1]), 'right'),
				'right': ((position[0][0] - 1, position[0][1]), 'left'),
				'center': ((position[0][0], position[0][1] - 1), 'down')
			}
		if direction == 'up':
			return {
				'left': ((position[0][0] - 1, position[0][1]), 'left'),
				'right': ((position[0][0] + 1, position[0][1]), 'right'),
				'center': ((position[0][0], position[0][1] + 1), 'up')
			}
		if direction == 'right':
			return {
				'left': ((position[0][0], position[0][1] + 1), 'up'),
				'right': ((position[0][0], position[0][1] - 1), 'down'),
				'center': ((position[0][0] + 1, position[0][1]), 'right')
			}
		if direction == 'left':
			return {
				'left': ((position[0][0], position[0][1] - 1), 'down'),
				'right': ((position[0][0], position[0][1] + 1), 'up'),
				'center': ((position[0][0] - 1, position[0][1]), 'left')
			}
	
	
	count = 0
	while not robot.go():
		robot.turn_right()
		count += 1
	
	robot.turn_right().turn_right().go()
	if count == 1:
		robot.turn_left()
	else:
		robot.turn_left().turn_left()
	
	
	while not robot.found():
		while True:
			if robot.found():
				return
			
			if position is None:
				position = steps[-1]
			location = create_location(position)
			
			if location['right'][0] not in [e[0] for e in steps] and robot.turn_left().go():
				if position != steps[-1]:
					del steps[steps.index(position)]
					steps.append(position)
				else:
					position[1] = True
				direction = location['right'][1]
				steps.append([location['right'][0], False, direction])
			elif location['left'][0] not in [e[0] for e in steps] and robot.turn_right().turn_right().go():
				if position != steps[-1]:
					del steps[steps.index(position)]
					steps.append(position)
				else:
					position[1] = True
				direction = location['left'][1]
				steps.append([location['left'][0], False, direction])
			elif location['center'][0] not in [e[0] for e in steps] and robot.turn_left().go():
				if position != steps[-1]:
					del steps[steps.index(position)]
					steps.append(position)
				steps.append([location['center'][0], False, direction])
			else:
				break
			
			position = None
		
		
		if not is_opposite(position):
			robot.turn_right().turn_right().go()
		
		for i in range(steps.index(position) - 1, -1, -1):
			if steps[i][1]:
				position = steps[i]
				break
			robot.go()
		
		if direction == 'up':
			direction = 'down'
		elif direction == 'down':
			direction = 'up'
		elif direction == 'right':
			direction = 'left'
		elif direction == 'left':
			direction = 'right'
