# MAIN METHOD FOR SHIA
#
#
import fileinput
import db
#import readline
import Restaurant
import Api

class MOD(object):
	def __init__(self, name):
		self.name = name
		self.subjs = []
		self.cmds = []

current_working_command = ""
def main():
	#Array of MOD Objects
	modules = []
	#modName holds the module current module being read in from config file
	modName = ""        
	for line in fileinput.input("Config.txt"):
		#Modules
		line = line.lower()
		if line[0] == '%':	 
			modName = line[1:].rstrip('\n')
			newMod = MOD(modName)
			modules.append(newMod)
		#Commands
		if line[0] == '$':
			indx = modules.index(newMod)
			modules[indx].cmds.append(line[1:])
		#Objects
		if line[0] == '#':
			indx = modules.index(newMod)
			modules[indx].subjs.append(line[1:])
				
	#Database creation from config
	tree = db.Tree()
	tree.createTree(modules)
	tree.printTree()
	
	#Main program flow -- Module executions will be called in here 
	while True:
		cmds = userInput(tree)
		crossRef = crossReference(cmds)
		print "EXECUTION DICT: \n", crossRef

		for key in crossRef:
			sub = key
			cmds = crossRef[key]
			print sub.module, "##########"
			if sub.module in Api.validAPIs:
				print "bitchass"
				Api.cmd = current_working_command
				print Api.cmd
				Api.validAPIs[sub.module]
		#CREATE EXECUTION HERE

#
# Recognize user input against DB Values
#  
def userInput(tree):
	user_input = raw_input()
	current_working_command = user_input
	print current_working_command
	user_input = user_input.split(" ")
	print "USER COMMANDS"
	print user_input
	valid_input = []
	for i in user_input:
		found = tree.searchTree(i)
		if found != None:
			valid_input.append(found)
	for i in valid_input:
		print i
	print "User Input-- Valid Input:"
	print valid_input
	print
	return valid_input

#
# Match valid subjects with their commands
# Form an execution  
#
def crossReference(valid_input):
	cmds = []
	subjs = []
	execute = {}
	#Sort valid input into subj/cmd
	for i in valid_input:
		if i.typ == "SBJ":
			subjs.append(i)
		elif i.typ == "CMD":
			cmds.append(i)
	print "Cross Ref here"
	print "Subs: ", subjs
	print "Cmds: ", cmds
	print
	#Cross Reference
	for x in subjs:
		a = []
		for j in cmds:
			if j.module == x.module:
				a.append(j)
		execute[x] = a
	return execute	
		
if __name__ == "__main__": main()
