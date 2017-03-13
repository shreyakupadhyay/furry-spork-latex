
'''
Author : Harika Rajavaram
Email : harika.rajavaram@gmail.com
Subject : reducing nodes
Description: Reduction of nodes to minimized number of nodes by updating the dictionary loaded from 
the json file and giving new output as json.

'''


import json

graphFile = open('../graph2.json','r')
# loading the file in json format and reading it
readFile = graphFile.read()

file_string = json.loads(readFile)
newNodes = ["A","B",["C","E"],["D","F"],"G"]


'''
combining all nodes in a block and calling update_json function
'''

def combine(stablility):
	for node in newNodes:
		if(len(node) == 1):   # if an array index contains only one element not the list
			continue
		else:	
			updated_node = ','.join(map(str, node)) # joining all nodes in a block
			equinode = node[0]    # calling function update_json with first element of an equivalent block
			# print updated_node,equinode
			update_nodeName(updated_node,equinode,stablility) #update node to updated_node

'''
updating the input json with removing the initial nodes with the equivalent blocks
'''

def update_nodeName(updated_node,node,stablility):
	stable_nodes = file_string[stablility][0].keys()
	count = 0
	for key in stable_nodes:
		if (key in updated_node and count==1): # updating the node with updated_node
			del file_string[stablility][0][key]
			
		elif (key in updated_node and count==0):  # remove the node if its equivalent node was updated 
			file_string[stablility][0][updated_node] = file_string[stablility][0][node]
			del file_string[stablility][0][node]
			count = 1
			# print file_string["stable"]

'''
updating the nodes outputs to the updated nodes
'''

def update_toNodes(stablility,stablility_keys):
	for key in stablility_keys:
		for idx in range(0,2): # as we are working for a DFA for hard coded outputs will be 2
			to_val = file_string[stablility][0][key][idx]["to"]
			for sub in nodeNames:
				if(to_val in sub):
					file_string[stablility][0][key][idx]["to"] = sub


if __name__ == "__main__":
	combine("stable")
	combine("unstable")
	stable_keys = file_string["stable"][0].keys()
	unstable_keys = file_string["unstable"][0].keys()
	nodeNames = stable_keys + unstable_keys
	update_toNodes("stable",stable_keys)
	update_toNodes("unstable",unstable_keys)
	print file_string