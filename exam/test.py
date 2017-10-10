from maze_runner import MazeRunner
from maze_controller import maze_controller

def test1():
	maze_example1 = {
    	'm': [
        	[0,1,0,0,0],
        	[0,1,1,1,1],
        	[0,0,0,0,0],
        	[1,1,1,1,0],
        	[0,0,0,1,0],
    	],
    	's': (0,0),
    	'f': (4,4)
	}
	maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])
	maze_controller(maze_runner)
	return maze_runner.found()

def test2():
	maze_example2 = {
    	'm': [
        	[0,0,0,0,0,0,0,1],
        	[0,1,1,1,1,1,1,1],
        	[0,0,0,0,0,0,0,0],
        	[1,1,1,1,0,1,0,1],
        	[0,0,0,0,0,1,0,1],
        	[0,1,0,1,1,1,1,1],
        	[1,1,0,0,0,0,0,0],
        	[0,0,0,1,1,1,1,0],
    	],
    	's': (7,7),
    	'f': (0,0)
	}
	maze_runner = MazeRunner(maze_example2['m'], maze_example2['s'], maze_example2['f'])
	maze_controller(maze_runner)
	return maze_runner.found()
	
def test3():
	maze_example3 = {
    	'm': [
        	[0,0,0,0,0,0,0,0,0,0,0],
        	[1,0,1,1,1,0,1,1,1,0,1],
        	[1,0,1,0,0,0,0,0,1,0,1],
        	[1,0,1,0,1,0,1,0,1,0,1],
        	[1,0,1,0,1,0,1,0,1,0,1],
        	[1,0,1,0,1,0,1,0,1,0,1],
        	[1,0,1,0,1,0,1,0,1,0,1],
        	[1,0,1,0,1,0,1,0,1,0,1],
        	[1,0,1,0,1,0,1,0,1,0,1],
        	[1,0,1,0,1,1,1,0,1,0,1],
        	[1,0,1,0,0,0,0,0,1,0,1],
    	],
    	's': (0,5),
    	'f': (10,5)
	}
	maze_runner = MazeRunner(maze_example3['m'], maze_example3['s'], maze_example3['f'])
	maze_controller(maze_runner)
	return maze_runner.found()

def test4():
	maze_example4 = {
    	'm': [
        	[0,0,0,0,1,0,1,0,0,0,0],
        	[0,1,1,1,1,0,1,1,1,1,0],
        	[0,0,0,0,0,0,0,0,0,0,0],
        	[0,1,0,1,1,1,1,1,0,1,0],
        	[1,1,0,1,0,0,0,1,0,1,1],
        	[0,1,0,1,0,1,0,1,0,1,0],
        	[0,1,0,0,0,1,0,0,0,1,0],
        	[0,1,0,1,1,1,1,1,0,1,0],
        	[0,1,0,0,0,0,0,0,0,1,0],
        	[0,1,1,1,1,0,1,1,1,1,0],
        	[0,0,0,0,0,0,0,0,0,0,0],
    	],
    	's': (0,5),
    	'f': (4,5)
	}
	maze_runner = MazeRunner(maze_example4['m'], maze_example4['s'], maze_example4['f'])
	maze_controller(maze_runner)
	return maze_runner.found()

def test5():
	maze_example5 = {
    	'm': [
        	[0,0,0,1,1,0,1,1,0,0,0],
        	[0,1,0,0,0,0,0,0,0,1,0],
        	[0,1,0,1,1,1,1,1,0,1,0],
        	[0,0,0,1,0,0,0,1,0,0,0],
        	[0,0,1,1,0,0,0,1,1,0,0],
        	[0,0,1,0,0,0,0,0,1,0,0],
        	[0,0,1,0,1,0,1,0,1,0,0],
        	[0,0,1,0,0,0,0,0,1,0,0],
        	[0,0,1,1,1,0,1,1,1,0,0],
        	[0,0,0,0,0,0,0,0,0,0,0],
        	[0,0,1,0,1,0,1,0,1,0,0],
    	],
    	's': (0,5),
    	'f': (4,5)
	}
	maze_runner = MazeRunner(maze_example5['m'], maze_example5['s'], maze_example5['f'])
	maze_controller(maze_runner)
	return maze_runner.found()

print('test1', test1())
print('test2', test2())
print('test3', test3())
print('test4', test4())
print('test5', test5())
