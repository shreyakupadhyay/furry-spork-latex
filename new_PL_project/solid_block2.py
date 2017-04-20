'''
Finding a solid shape block
'''

rows = 7  # number of rows of matrix
cols = 7  # number of columns of matrix
extra = 0
sides = 0

matrix = [[1, 1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 0, 1],
          [1, 1, 1, 1, 1, 0, 1],
          [0, 0, 1, 0, 0, 0, 1],
          [0, 0, 1, 1, 1, 1, 1]]

hor = 	 [[1, 2, 3, 4, 5, 0, 0],
          [1, 2, 3, 4, 5, 0, 0],
          [1, 2, 3, 4, 5, 6, 7],
          [1, 2, 3, 4, 5, 0, 1],
          [1, 2, 3, 4, 5, 0, 1],
          [0, 0, 1, 0, 0, 0, 1],
          [0, 0, 1, 2, 3, 4, 5]]

ver = 	 [[1, 1, 1, 1, 1, 0, 0],
          [2, 2, 2, 2, 2, 0, 0],
          [3, 3, 3, 3, 3, 1, 1],
          [4, 4, 4, 4, 4, 0, 2],
          [5, 5, 5, 5, 5, 0, 3],
          [0, 0, 6, 0, 0, 0, 4],
          [0, 0, 7, 1, 1, 1, 5]]


def horizontal():
	max_len = 0
	for row in range(0,rows):
		count_len = 0
		for col in range(0,cols):
		    if (matrix[row][col] == 1):
		        count_len = count_len + 1
	          	matrix[row][col] = count_len
		    else:
		    	count_len = 0
	print matrix

def vertical():
	max_len = 0
	for col in range(0,cols):
		count_len = 0
		for row in range(0,rows):
		    if (matrix[row][col] == 1):
		        count_len = count_len + 1
	          	matrix[row][col] = count_len
		    else:
		    	count_len = 0
	print matrix

if __name__ == "__main__":
	# horizontal()
	vertical()