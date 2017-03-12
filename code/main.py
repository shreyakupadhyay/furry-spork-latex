'''
Author : Harika Rajavaram
Email : harika.rajavaram@gmail.com
Subject : Main File
Description: rules to generate latex code for nodes, edges (location of node and edge placement is hardcoded)
'''

import json

graphFile = open('../graph2.json','r')
# loading the file in json format and reading it
file_string = json.loads(graphFile.read())
stable_nodes = file_string["stable"][0].keys()
unstable_nodes = file_string["unstable"][0].keys()
nodes = stable_nodes + unstable_nodes

# pre-defined input alphabet
alphabet = ["0","1"]

#for i in stable_nodes:
#	print file_string["stable"][0][i][0]
#	print file_string["stable"][0][i][1]

def genbegin():
	print "\\begin{document}"
	print "\\begin{center}"

# function to generate nodes
def genNodes(nodes,Refnode,direction):
	for nodeName in nodes:
		print genNodeState(nodeName) + nodeName + genNodeLoc(Refnode,direction) + genNodeVar(nodeName)

# hepler function for genNodes function
def genNodeVar(nodeName):
	return " {$"+nodeName+"$}";

# hepler function for genNodes function
def genNodeLoc(Refnode,direction):
	return  " ["+direction+"="+Refnode+"]" 

# hepler function for genNodes function
def genNodeState(nodeName):
	if(nodeName in stable_nodes):
		return "\\node[state,accepting] "
	else:
		return "\\node[state] "

# function to generate edges
def genEdges(stable_nodes,unstable_nodes,alphabet,direction,angle):
	for nodeName in stable_nodes:
		for i in alphabet:	
			print nodeName + genEdgeLoc(direction,angle,i) +  file_string["stable"][0][nodeName][int(i)]["to"]
	for nodeName in unstable_nodes:
		for i in alphabet:	
			print nodeName + genEdgeLoc(direction,angle,i) +  file_string["unstable"][0][nodeName][int(i)]["to"]

# hepler function for genEdges function
def genEdgeLoc(direction,angle,input):
	return " egde " + "["+direction+"="+angle+"] node {"+ input +"} " 



#invoking the functions
genbegin()
genNodes(nodes,"A","right of")
print "\path"
genEdges(stable_nodes,unstable_nodes,alphabet,"bend left","20")