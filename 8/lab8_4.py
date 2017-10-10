def make_sudoku(size):
	sudoku = []
	tmp = [[j for j in range(size * (i - 1) + 1, size * i + 1)] for i in range(1, size + 1)]
	
	for i in range(size):
		for j in range(size):
			sudoku.append(sum(tmp, []))
			first = tmp[0]
			tmp = tmp[1:]
			tmp.append(first)
		
		for i in range(len(tmp)):
			first = tmp[i][0]
			tmp[i] = tmp[i][1:]
			tmp[i].append(first)
	
	return sudoku


def gprint(list_):
	for i in list_:
		print(i)


gprint(make_sudoku(1)) # [[1]]
gprint(make_sudoku(2)) # [[1,2,3,4],[3,4,1,2],[2,1,4,3],[4,3,2,1]]
gprint(make_sudoku(3)) # [[3,5,8,1,2,7,6,4,9],[6,7,4,5,8,9,3,2,1],[2,1,9,3,4,6,5,7,8],[9,8,6,7,1,4,2,5,3],[4,3,1,2,6,5,8,9,7],[7,2,5,9,3,8,1,6,4],[1,6,3,4,7,2,9,8,5],[8,9,7,6,5,1,4,3,2],[5,4,2,8,9,3,7,1,6]]