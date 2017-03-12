
'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : algorithm for minimising dfa
Description:
Minimizing DFA using equivalent blocks and returning multi dimensional list which contains equivalent blocks. 
'''
import json

graphFile = open('../graph2.json','r')

json_obj = json.loads(graphFile.read())

'''
check if a value(0,1) exists in a dictionary
'''
def checkval(dic,x,val,nodes,stability1,stability2):   # transition function to know for input 0,1 to which node(stable,unstable) output is going.
	if val in dic[x].values(): 
		if(dic[x]["to"] in nodes): # getting "to" values
			return stability1
		if(dic[x]["to"] not in nodes):
			return stability2 
	else: return False

'''
generating list containing the conditions whether the transitions with inputs (0,1)
is stable or unstable and comparing them to find equivalence.
'''
def checkequi(node1,node2,nodes,stability1,stability2):
	alphabet = [0,1] # or 1
	node1_val = []
	node2_val = []
	for val in alphabet:
			for x in range(len(node1)):
				value = checkval(node1,x,val,nodes,stability1,stability2)
				if(value!=False):
					node1_val.append(value)
			for x in range(len(node2)):
				value = checkval(node2,x,val,nodes,stability1,stability2)
				if(value!=False):
					node2_val.append(value) # node1 = "D"
	
	if(node1_val==node2_val):
		print "HURRah"
		return True
	else:
		print "NO"
		return False

'''
converting multidimensional list into 1-D list
'''
def listsearch(blocks):
	nodes_blocks = []
	for ele_1 in blocks:
		for ele_2 in ele_1:
			nodes_blocks.append(ele_2)
	return nodes_blocks

'''
main function to call other functions with various arguments
'''
def transition(stability1,stability2):
	nodes = json_obj[stability1][0].keys() # nodes with particular stability
	blocks = []
	for idx_1 in range(0,len(nodes)-2):
		equi_nodes = [nodes[idx_1]]
		
		for idx_2 in range(idx_1+1,len(nodes)):  # selecting two nodes to compare for quivalence
			node1 = json_obj[stability1][0][nodes[idx_1]] # "D"
			node2 = json_obj[stability1][0][nodes[idx_2]] # "F"
			result_equi = checkequi(node1,node2,nodes,stability1,stability2)
			if(result_equi):
				# equi_nodes.append(nodes[idx_1]) # generating equivalence blocks
				equi_nodes.append(nodes[idx_2])
		
		blocks.append(equi_nodes)
	return blocks





if __name__ == "__main__":
	unstable_block = transition("unstable","stable")
	stable_block = transition("stable","unstable")
	all_nodes = json_obj["stable"][0].keys() + json_obj["unstable"][0].keys() # all nodes

	all_nodes = [x for x in all_nodes if x not in listsearch(stable_block)] # removing stable blocks(blocks generated from stable nodes list) from all_nodes
	all_nodes = [x for x in all_nodes if x not in listsearch(unstable_block)] # removing unstable blocks(blocks generated from unstable nodes list) from all_nodes

	print all_nodes + unstable_block + stable_block # generating list required of reduction [u'G', u'B', [u'A'], [u'C', u'E'], [u'D', u'F']]


