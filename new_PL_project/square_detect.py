'''
0 0 0 0 0 0
0 1 1 1 0 0
0 1 0 1 0 0
0 1 1 1 0 0
0 0 0 0 0 0
0 0 0 0 0 0


0 0 0 0 0 0
0 0 1 0 0 0
0 1 1 1 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0


Left right up down right-up left-up right-down left-down 
'''

rows = 6
cols = 6
extra = 0
sides = 0
#matrix = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0]]
matrix = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]
#print matrix
#matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0]]
'''
rows = 7
cols = 7
extra = 0
sides = 0
matrix = [[1, 1, 1, 1, 1, 0, 0],[1, 0, 0, 0, 1, 0, 0],[1, 0, 1, 1, 1, 1, 1],[1, 0, 1, 0, 1, 0, 1],[1, 1, 1, 1, 1, 0, 1],
[0, 0, 1, 0, 0, 0, 1],[0, 0, 1, 1, 1, 1, 1]]
'''
coordinates = []

def motion(next_row,next_col,prev_node,row,col,direction,count,prev_dir):
    global sides
    if (extra == 1):
        return
#    print extra
    count = count+1
    next_dir = direction
#    print prev_dir + "   " + direction
    next_node = (next_row, next_col)
    global coordinates
    if next_node != prev_node:
        print next_node, prev_node
        if (prev_dir != direction):
            sides = sides + 1
            coordinates.append((row,col))            
            print "change in direction"
        decision(next_row, next_col, next_dir, (row, col), start_node,count)



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

                        # \draw (a.center) -- (b.center) -- (c.center) -- cycle;


def decision(row, col, prev_dir, prev_node,start_node,count):  # this function decides which direction to choose and move forward.

    # [row][col] current location
    global extra
    if (start_node == prev_node and count>1):
 #       print "stopped"
        extra = 1
        return extra

    if(extra == 1):
        return extra

    if row + 1 < rows and matrix[row + 1][col] == 1:  # [row+1][col]   down
        motion(row + 1 , col, prev_node, row, col, 'd',count,prev_dir)


    if row - 1 > 0 and matrix[row - 1][col] == 1:  # [row-1][col]  up
        motion(row - 1, col, prev_node, row, col, 'u',count,prev_dir)


    if col + 1 < cols and matrix[row][col + 1] == 1:  # [row][col+1]  right
        motion(row, col+1, prev_node, row, col, 'r',count,prev_dir)


    if col - 1 > 0 and matrix[row][col - 1] == 1:  # [row][col-1]  left
        motion(row , col-1 , prev_node, row, col, 'l',count,prev_dir)


    if row + 1 < rows and col + 1 < cols and matrix[row + 1][col + 1] == 1:  # [row+1][col+1]  right-down
        motion(row + 1, col+1 , prev_node, row, col, 'rd',count,prev_dir)


    if row - 1 > 0 and col - 1 > 0 and matrix[row - 1][col - 1] == 1:  # [row-1][col-1]  left-up
        motion(row - 1, col - 1, prev_node, row, col, 'lu',count,prev_dir)


    if row + 1 < 0 and col + 1 < cols and matrix[row - 1][col + 1] == 1:  # [row-1][col+1]  right-up
        motion(row - 1, col + 1, prev_node, row, col, 'ru',count,prev_dir)


    if row + 1 < rows and col - 1 > 0 and matrix[row + 1][col - 1] == 1:  # [row+1][col-1]  left-down
        motion(row + 1, col - 1, prev_node, row, col, 'ld',count,prev_dir)

if __name__ == "__main__":
    count = 0
    for row in range(rows):
        for col in range(cols):
            if (matrix[row][col] == 0):
                continue
            elif (matrix[row][col] == 1):
                start_node = (row, col)
                decision(row, col, '', (row, col - 1), start_node,0)
                break
        if (count == 1):
            break
    print coordinates
    print "Number of Sides = " + str(sides-1)
    print latex_code(coordinates)


