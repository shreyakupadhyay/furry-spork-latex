'''
Description: Detecting squares from a 2D matrix.
Working status: Final working code for detecting squares in 2-D matrix.
'''
# and start_node != (row,col))

import sys
# import pandas as pd

coordinates = []
#pts = []
lines = []

extra, sides = 0,0

matrix = []
checks = []
filename = sys.argv[1] # matrix.txt


'''
reading matrix from a file.
'''
def readInput():
  raw_mat = []
  f = open(filename)
  for line in f.readlines():
      raw_mat.append(line.split())
  f.close()
  for row in raw_mat:
      matrix.append([i for i in row if i.isdigit()])
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
         matrix[i][j]=int(matrix[i][j])

''' 
initialising the checks matrix
'''
def initCheck():
  global checks
  checks = [[0 for x in range(cols)] for y in range(rows)]

'''
removing duplicates from list and also preserving the order
'''
def removeDuplicates(myList):
    newlist = []
    for element in myList:
       if element not in newlist:
           newlist.append(element)
    return newlist

'''
Getting number of ones surrounding a point in a matrix.
'''
def numOnes(row,col):
  num_ones = 0
  if row + 1 < rows and matrix[row + 1][col] == 1:
    num_ones = num_ones + 1

  if row - 1 >= 0 and matrix[row - 1][col] == 1:
    num_ones = num_ones + 1

  if col + 1 < cols and matrix[row][col + 1] == 1:
    num_ones = num_ones + 1

  if col - 1 >= 0 and matrix[row][col - 1] == 1:
    num_ones = num_ones + 1

  # print num_ones
  return num_ones 

'''
movement of pointer in a direction at particular coordinate
'''
def motion(next_row,next_col,prev_node,row,col,direction,count,prev_dir,start_node,corner):
    global sides
    if (extra == 1):
        return
    count = count+1
    next_dir = direction  
    next_node = (next_row, next_col)
    # print pd.DataFrame(checks)
    # print "====================="
    global coordinates
    if next_node != prev_node:
        checks[row][col] = checks[row][col] + 1
        if (prev_dir != direction or numOnes(row,col)>=3):
            sides = sides + 1
            coordinates.append((row,col))
            prev_corner = corner
            corner = (row,col)
#            print (prev_corner,corner)
            if(prev_corner != corner):
              lines.append(tuple((prev_corner,corner))) 
#            pts.append(tuple((row,col)))
        decision(next_row, next_col, next_dir, (row, col), start_node,count,corner)

'''
making decision to go in a direction using various creteria
'''
def decision(row, col, prev_dir, prev_node,start_node,count,corner):

    # [row][col] current location
    global extra # breaking recursion.
    if (start_node == prev_node and count>1):
        extra = 1
        return extra

    if(extra == 1):
        return extra


    if row + 1 < rows and matrix[row + 1][col] == 1 and checks[row + 1][col]<=(numOnes(row+1,col)-1):  # [row+1][col]   down
        motion(row + 1 , col, prev_node, row, col, 'd',count,prev_dir,start_node,corner)

    if row - 1 >= 0 and matrix[row - 1][col] == 1 and checks[row - 1][col]<=(numOnes(row-1,col)-1):  # [row-1][col]  up
      motion(row - 1, col, prev_node, row, col, 'u',count,prev_dir,start_node,corner)


    if col + 1 < cols and matrix[row][col + 1] == 1 and checks[row][col+1]<=(numOnes(row,col+1)-1):  # [row][col+1]  right
        motion(row, col+1, prev_node, row, col, 'r',count,prev_dir,start_node,corner)


    if col - 1 >= 0 and matrix[row][col - 1] == 1 and checks[row][col-1]<=(numOnes(row,col-1)-1):  # [row][col-1]  left
        motion(row , col-1 , prev_node, row, col, 'l',count,prev_dir,start_node,corner)

'''
Iterating through matrix.
'''
def iterMatrix():
  row, col, count = 0,0,0
  for row in range(0,rows):
      for col in range(0,cols):
          if (matrix[row][col] == 0):
              continue
          elif (matrix[row][col] == 1):
              start_node = (row, col)
              corner = start_node
              decision(row, col, '', (row, col - 1), start_node,0,corner)
              break
      if (count == 1):
          break

if __name__ == "__main__":
    readInput()
    global rows,cols
    rows = len(matrix)  # number of rows of matrix
    cols = len(matrix[0])  # number of columns of matrix
    initCheck()
    iterMatrix()
#    print [line for line in set(lines)]
    unique_lines = removeDuplicates(lines)
    for l in unique_lines:
      print l
