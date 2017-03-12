
'''
Author : Harika Rajavaram
Email : harika.rajavaram@gmail.com
Subject : reducing nodes
Description: Reduction of nodes to minimized number of nodes by updating the dictionary loaded from 
the json file and giving new output as json.

'''
# [[A],[B],[C,E],[D,F],[G]]

import json

graphFile = open('../graph2.json','r')
# loading the file in json format and reading it
readFile = graphFile.read()

# file_string = json.loads(readFile)
string = '''{
	"stable":[{
		"D":[{"val":1,"to":"E"},{"val":0,"to":"D"}],
		"F":[{"val":1,"to":"E"},{"val":0,"to":"D"}],
		"G":[{"val":1,"to":"G"},{"val":0,"to":"F"}]
		}],
	"unstable":[{
		"A":[{"val":0,"to":"B"},{"val":1,"to":"C"}],
		"B":[{"val":1,"to":"E"},{"val":0,"to":"D"}],
		"C":[{"val":0,"to":"F"},{"val":1,"to":"G"}],
		"E":[{"val":1,"to":"G"},{"val":0,"to":"F"}]
		}]
}'''
file_string = json.loads(string)
newNodes = ["A","B",["C","E"],["D","F"],"G"]
# print newNodes[0]



def fucn(stablility):
	for node in newNodes:
		if(len(node) == 1):
			continue
		else:	
			updated_node = ','.join(map(str, node))
			equinode = node[0]
			print updated_node,equinode
			update_json(updated_node,equinode,"unstable") #update node to updated_node


def update_json(updated_node,node,stablility):
	stable_nodes = file_string[stablility][0].keys()
	count = 0
	for key in stable_nodes:
		if (key in updated_node and count==1):
			del file_string[stablility][0][key]
			print key,"if"
		elif (key in updated_node and count==0): 
			file_string[stablility][0][updated_node] = file_string[stablility][0][node]
			del file_string[stablility][0][node]
			count = 1
			print key,"elif"
			# print file_string["stable"]
	print file_string[stablility]

fucn("stable")
			
# afterRed(newNodes)

# nodes = stable_nodes + unstable_nodes

# for i in range(0,len(stable_nodes)):
# 	if(file_string["stable"][0][i] == "D" or file_string["stable"][0][i] == "F"):
# 		print "in if"
# 		file_string["stable"][0]["D,F"] = file_string["stable"][0].pop("D")
# 		del file_string["stable"][0].keys()[i]


# print file_string["stable"][0].keys()
