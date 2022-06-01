
 

class Node():
	def __init__(self,value):
		
		self.value = value
		self.next = None
		return 



class Stack():
	def __init__(self):
		
		self.pointer = None
		self.index = -1
		return 

	

	def Empty(self):
		if self.index == -1:
			return True
		
		else:
			return False


	
	def Travel(self):
		
		currentNode = self.pointer
		List= None
		depth = 0
		
		while currentNode!=None:
			
			depth+=1
			
			if 	depth == 1:
				List = str(currentNode.value)

			else:
				List += "-" + str(currentNode.value)

			currentNode= currentNode.next	
		
		return List



	def Push(self,value):
		
		node = Node(value)

		if  self.pointer == None:
			self.pointer = node
		
		else:
			node.next = self.pointer
			self.pointer = node

		self.index +=1



	def Pop(self):
		
		currentNode = self.pointer
		
		if currentNode == None:
			return False

		else:
			self.index-=1
			self.pointer = currentNode.next
			return currentNode.value

		
