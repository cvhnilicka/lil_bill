
import difflib

class ObjectNode(object):
	def __init__(self, typ, module, value, standalone):
		self.module = module
		self.typ = typ    
		self.valueStr = value
		self.standalone = standalone

	def __str__(self):
        	return str(self.__dict__)	

	def __eq__(self, other): 
        	return self.__dict__ == other.__dict__

class ModuleNode(object):
	
	def __init__(self, name):
		self.name = name
		#Lists of valid commands and subjects
		self.commands = [] 
		self.subjects = []
	
	def addCmd(self, cmd_add, stdaln):
		newN = ObjectNode("CMD", self.name, cmd_add)	
		self.commands.append(newN)  	
	
	def addSbj(self, subject_add):
		newN = ObjectNode("SBJ", self.name, subject_add)	
		self.subjects.append(newN)
	
	## EVENTUALLY MAKE THIS FASTER ##
	def search(self, string):					
			for i in self.commands:
				if difflib.SequenceMatcher(None, i.valueStr, string).ratio() > .80:
					return i
			for j in self.subjects:
				if difflib.SequenceMatcher(None, j.valueStr, string).ratio() > .80:
					return j

	def printObjs(self):
		for i in self.commands: 
			print "--|-- CMD: --"
			print i
		for x in self.subjects:
			print "--|-- SBJ: --"
			print x

class RootNode(object):
	def __init__(self):
		self.modules = []
		
	def addModule(self, moduleName, cmdarr, sbjarr):
		newMod = ModuleNode(moduleName)
		print moduleName
		print "Command array from config: ", cmdarr, "\n" 
		for i in cmdarr:
			if "*" in i:
				i = i[:-1]
				newMod.addCmd(i, True)
			else:
				newMod.addCmd(i, False)                       #Fills the module node's commands array 
			
		print moduleName
		print "Sub array from config: ",sbjarr,"\n"
		for j in sbjarr:			
			newMod.addSbj(j)			#Fills the module node's obj array 		
		self.modules.append(newMod)		
	
	def searchModule(self, moduleName): 
		for i in self.modules:
			if i.name == moduleName:
				return i

class Tree(object):

	def __init__(self):
		self.head = RootNode()
	

	def createTree(self, modulearr):
		modulearr.sort(key = lambda x: x.name)
		for i in modulearr:
			self.head.addModule(i.name, i.cmds, i.subjs)
					
	def searchTree(self, string):
		string.lower()		

		for i in self.head.modules:
			found = i.search(string)
			if found != None:
				break
		return found		
 
	def printTree(self):
		print "---ROOT---"
		for i in self.head.modules:
			print "|-MODULE-", i.name
			i.printObjs()
