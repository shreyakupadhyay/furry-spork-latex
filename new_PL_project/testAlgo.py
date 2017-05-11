import sys
import genLatexCode
import lineSegments
from shapely.ops import polygonize
from math import sqrt

def distance(a,b):
	(x1,y1) = a
	(x2,y2) = b
	return sqrt(pow(x1-x2,2) + pow(y1-y2,2))

def cost(start,end,line):
	(a,b) = line
	if(a != start and a != end):
		return distance(start,a) + distance(end,a)
	elif(b != start and b != end):
		return distance(start,b) + distance(end,b)

def cost2(start,end,line):
	(a,b) = line
	if(start in line and start != []):
		return distance(end,a)
	elif(b != start and b != end):
		return distance(start,b) + distance(end,b)

def findNext(start,end, lines):
	return filter(lambda line: end in line or start in line, lines)

def updateEnds(start,end,line):
	if start in line:
		if start == line[0]:
			start = line[1]
		else:
			start = line[0]
	else:
		if end == line[0]:
			end = line[1]
		else:
			end = line[0]
	return (start,end)

if __name__ == "__main__":
	lines = lineSegments.main(sys.argv[1])
	print lines
	nset = []
	nset.append(lines.pop(0))
	(start,end) = nset[0]
	while(start != end):
		selected = max(map(lambda line: (cost(start,end,line),line), findNext(start,end,lines)),key=lambda s: s[0])
		nset.append(lines.pop(lines.index(selected[1])))
		print start,end
		(start,end) = updateEnds(start,end,nset[-1])
	print nset