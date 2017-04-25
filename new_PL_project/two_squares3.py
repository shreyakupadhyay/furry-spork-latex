'''
Final working code for detecting squares in 2-D matrix.
'''

'''
1 1 1 1 1 0 0
1 0 0 0 1 0 0
1 0 1 1 1 1 1
1 0 1 0 1 0 1
1 1 1 1 1 0 1
0 0 1 0 0 0 1
0 0 1 1 1 1 1
output: (2, 6), (6, 6), (3, 0), (4, 4), (0, 0), (2, 0), (6, 2), (0, 4), (2, 2), (4, 2), (1, 0), (2, 4), (4, 0)
'''
rows = 7  # number of rows of matrix
cols = 7  # number of columns of matrix
extra = 0
sides = 0

# '''
matrix = [[1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 0, 1, 0, 0],
          [1, 0, 1, 1, 1, 1, 1],
          [1, 0, 1, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 0, 1],
          [0, 0, 1, 0, 0, 0, 1],
          [0, 0, 1, 1, 1, 1, 1]]
'''

matrix = [[1, 1, 1, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 0, 1, 0, 1, 0, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]
'''
checks = [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]

coordinates = [(0,0)]
pts = []
lines = []

from pandas import *
'''0
counting number of ones surrounding a point. And checking whether it have more than 2 ones.
If it has than it is a corner point.
'''
def numOnes(row,col):
  num_ones = 0
  if row + 1 < rows and matrix[row + 1][col] == 1:
    num_ones = num_ones + 1

  if row - 1 > 0 and matrix[row - 1][col] == 1:
    num_ones = num_ones + 1

  if col + 1 < cols and matrix[row][col + 1] == 1:
    num_ones = num_ones + 1

  if col - 1 > 0 and matrix[row][col - 1] == 1:
    num_ones = num_ones + 1

  # print num_ones
  return num_ones 


# movement of pointer in a direction at particular coordinate
def motion(next_row,next_col,prev_node,row,col,direction,count,prev_dir,start_node,corner):
    global sides
    if (extra == 1):
        return
    count = count+1
    next_dir = direction  
    next_node = (next_row, next_col)
    global coordinates
    if next_node != prev_node:
        checks[row][col] = checks[row][col] + 1
        # print DataFrame(checks)
        # print numOnes(row,col)
        if ((prev_dir != direction and start_node != (row,col)) or numOnes(row,col)>=3):
            sides = sides + 1
            coordinates.append((row,col))
            prev_corner = corner
            corner = (row,col)
            lines.append(tuple((prev_corner,corner))) 
            pts.append(tuple((row,col)))
            # print tuple((prev_corner,corner))
            # print (row,col)
        decision(next_row, next_col, next_dir, (row, col), start_node,count,corner)


# generating latex code using latex syntax
def latex_code(coordinates):
    append_code = "\draw "
    for coordinate in coordinates:
        append_code = append_code + str(coordinate)+" -- "
    append_code =append_code + "cycle\n"

    code = """\documentclass{article}
                \usepackage{tikz}
                \\begin{document}
                    \\begin{tikzpicture}"""+append_code+"""\end{tikzpicture}
                \end{document}"""
    return code


tups_of_pts = []
def points_for_lines(pts):
    i = 0
    while(i<(len(pts)-1)):
        tups_of_pts.append(tuple((pts[i],pts[i+1])))
        i=i+2
    return tups_of_pts


# making decision to go in a direction using various creteria
def decision(row, col, prev_dir, prev_node,start_node,count,corner):

    # [row][col] current location
    global extra
    if (start_node == prev_node and count>1):
        extra = 1
        return extra

    if(extra == 1):
        return extra

    if row + 1 < rows and matrix[row + 1][col] == 1 and checks[row + 1][col]<=(numOnes(row+1,col)-1):  # [row+1][col]   down
        # print "motion_down"
        motion(row + 1 , col, prev_node, row, col, 'd',count,prev_dir,start_node,corner)


    if row - 1 > 0 and matrix[row - 1][col] == 1 and checks[row - 1][col]<=(numOnes(row-1,col)-1):  # [row-1][col]  up
        # print "motion_up"
        motion(row - 1, col, prev_node, row, col, 'u',count,prev_dir,start_node,corner)

    if col + 1 < cols and matrix[row][col + 1] == 1 and checks[row][col+1]<=(numOnes(row,col+1)-1):  # [row][col+1]  right
        # print "motion_right"
        motion(row, col+1, prev_node, row, col, 'r',count,prev_dir,start_node,corner)


    if col - 1 > 0 and matrix[row][col - 1] == 1 and checks[row][col-1]<=(numOnes(row,col-1)-1):  # [row][col-1]  left
        # print "motion_left"
        motion(row , col-1 , prev_node, row, col, 'l',count,prev_dir,start_node,corner)

if __name__ == "__main__":
    count = 0
    row = 0
    col = 0
    for row in range(0,rows):
        for col in range(0,cols):
            if (matrix[row][col] == 0):
                continue
            elif (matrix[row][col] == 1):
                # print "Shreyaak"
                start_node = (row, col)
                corner = start_node
                decision(row, col, '', (row, col - 1), start_node,0,corner)
                break
        if (count == 1):
            break

    unique_pts = sorted(set(tups_of_pts),key=tups_of_pts.index)
    for i in set(lines):
      print i
    # print checks
#    print list(set(tups_of_pts))