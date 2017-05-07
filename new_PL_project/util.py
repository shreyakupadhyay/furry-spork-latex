import numpy as np
import sys
import genLatexCode
import lineSegments
from shapely.ops import polygonize
from shapely.geometry import mapping

if __name__ == "__main__":
	lines = lineSegments.main(sys.argv[1])
	all_shapes = ""
	for i in (list(polygonize(lines))):
		points = mapping(i.envelope)
		coordinates = ""
		for i in range(0,len(points["coordinates"][0])):
			coordinates = coordinates + str(points["coordinates"][0][i]) + " -- "
		coordinates = "\draw[orange, ultra thick] "+ coordinates + "cycle;"
		# print coordinates		
		all_shapes = all_shapes + coordinates + "\n"
	print all_shapes
	genLatexCode.latexCode(all_shapes)
