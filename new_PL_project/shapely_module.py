from shapely.ops import polygonize

for i in (list(polygonize(lines))):
	print i.envelope
