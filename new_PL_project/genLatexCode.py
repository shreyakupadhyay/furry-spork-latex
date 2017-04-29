'''
Description: Generating tikz code of a shape.
Working status: Currently we are able to work with square shapes. 
'''

'''
latexCode(shape_coordinates) function generates the tikz code of square.
'''

def latexCode(shape_coordinates):
	file = open("importLatexCode.txt", "r")
	searchline = "    \\begin{tikzpicture}\n"
	contents = file.readlines()
	index = contents.index(searchline)
	file.close()

	code = "\draw[orange, ultra thick] (2,0) -- (2,2) -- (0,2) -- (0,0) -- cycle;"
	contents.insert(index+1, code)

	file = open("outputLatexCode.txt", "w")
	contents = "".join(contents)
	file.write(contents)
	file.close()
# latexCode("")