'''
Author : Harika Rajavaram
Email : harika.rajavaram@gmail.com
Subject : Main File
Description: rules to generate latex code for nodes, edges (reference node, location of node and edge placement is hardcoded)
'''

import json

def genbegin():
	print "\\begin{document}"
	print "\\begin{center}"

# function to generate nodes
def genNodes(nodes,Refnode,direction,stable_nodes):
	for nodeName in nodes:
		print genNodeState(nodeName,stable_nodes) + nodeName + genNodeLoc(Refnode,direction) + genNodeVar(nodeName)

# hepler function for genNodes function
def genNodeVar(nodeName):
	return " {$"+nodeName+"$}";

# hepler function for genNodes function
def genNodeLoc(Refnode,direction):
	return  " ["+direction+"="+Refnode+"]" 

# hepler function for genNodes function
def genNodeState(nodeName,stable_nodes):
	if(nodeName in stable_nodes):
		return "\\node[state,accepting] "
	else:
		return "\\node[state] "

# function to generate edges
def genEdges(stable_nodes,unstable_nodes,alphabet,direction,angle,file_string):
	for nodeName in stable_nodes:
		for i in alphabet:	
			print nodeName + genEdgeLoc(direction,angle,i) +  file_string["stable"][0][nodeName][int(i)]["to"]
	for nodeName in unstable_nodes:
		for i in alphabet:	
			print nodeName + genEdgeLoc(direction,angle,i) +  file_string["unstable"][0][nodeName][int(i)]["to"]

# hepler function for genEdges function
def genEdgeLoc(direction,angle,input):
	return " egde " + "["+direction+"="+angle+"] node {"+ input +"} " 


# if __name__ == "__main__":
#invoking the functions
def main(DFA_json):
	alphabet = ["0","1"] # pre-defined input alphabet
	
	file_string = json.loads(DFA_json)
	# print file_string
	stable_nodes = file_string["stable"][0].keys()
	unstable_nodes = file_string["unstable"][0].keys()
	nodes = stable_nodes + unstable_nodes
	genbegin()
	genNodes(nodes,"A","right of",stable_nodes)
	print "\path"
	genEdges(stable_nodes,unstable_nodes,alphabet,"bend left","20",file_string)

# DFA_json = "{u'unstable': [{u'A': [{u'to': u'B', u'val': 0}, {u'to': 'C,E', u'val': 1}], 'C,E': [{u'to': 'D,F', u'val': 0}, {u'to': u'G', u'val': 1}], u'B': [{u'to': 'C,E', u'val': 1}, {u'to': 'D,F', u'val': 0}]}], u'stable': [{'D,F': [{u'to': 'C,E', u'val': 1}, {u'to': 'D,F', u'val': 0}], u'G': [{u'to': u'G', u'val': 1}, {u'to': 'D,F', u'val': 0}]}]}"
# main(DFA_json)