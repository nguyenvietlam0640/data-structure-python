




class Node():
	def __init__(self,value):
	
		self.value = value
		self.next = None
		return



class Queue():
	def __init__(self):

		self.first = None
		self.last = None
		self.index= -1
		return


	
	def Travel(self):
		
		List = None
		currentNode = self.first
		index = 0
		
		while currentNode!= None:
			index+=1
			if index ==1:
				List = str(currentNode.value)
			
			else:
				List += "<-" + str(currentNode.value)

			currentNode = currentNode.next
		
		return List

	

	def Empty(self):

		if self.index == -1 or self.first == None:
			return True
		
		else:
			return False

	

	def Add(self,value):
		
		node= Node(value)
		
		if  self.first == None:
			self.first = node
			self.last = node

		else:
			self.last.next = node
			self.last = node

		self.index += 1

	

	def Delete(self):
		
		currentNode = self.first
		
		if self.first != None:
			self.first = self.first.next
			self.index -= 1
			return currentNode.value

		else:

			return False



