def saddle_point(matrix):
	if not len(matrix):
		return False
	
	for i in range(len(matrix[0])):
		col = [matrix[k][i] for k in range(len(matrix))]
		
		for j in range(len(matrix)):
			if matrix[j][i] == min(matrix[j]) and matrix[j][i] == max(col) and col.count(matrix[j][i]) == 1 and matrix[j].count(matrix[j][i]) == 1:
				return (j, i)
	
	return False




print(saddle_point([[1,2,3],[3,2,1]]))
print(saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]]))
print(saddle_point([[21]]))