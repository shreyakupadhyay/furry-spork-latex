import sys
import genLatexCode
import lineSegments
from shapely.ops import polygonize

if __name__ == "__main__":
	lines = lineSegments.main(sys.argv[1])

	for i in (list(polygonize(lines))):
		print i.envelope
		
	genLatexCode.latexCode(lines)
