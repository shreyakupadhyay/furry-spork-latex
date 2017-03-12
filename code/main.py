import json

graphFile = open('../graph.json','r')
print json.loads(graphFile.read())["graph"][0].keys()
# with open(...) as libFile:
    # for line in libFile:
