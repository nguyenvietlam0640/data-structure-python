



globalIndex = None



class Node():
	def __init__(self,value):
		
		self.value = value
		self.nextPoint = None		
		return 


class createLinkList():
	def __init__(self):
		
		self.first= None
		self.last= None 
		return
	

	def addNode(self,value):
		
		node= Node(value)
		global globalIndex 
		
		if self.first== None:
			self.first = node 
			self.last = node 
			globalIndex =1
		
		else:
			self.last.nextPoint= node 
			self.last = node 
			globalIndex +=1
	

	def showList(self):
		
		index =0
		List = None
		currentNode= self.first
		
		while currentNode!= None:
			index +=1
			if index ==1:
				List = str(currentNode.value)
			else:
				List+= "->" +str(currentNode.value)
			currentNode = currentNode.nextPoint
		
		print("["+ str(List) +"]")

	
	def insertionNode(self,index,value):
		
		global globalIndex
		node = Node(value)
		firstNode = self.first
		currentNode= self.first
		currentIndex =2

		try:
			if index<=globalIndex:
				while currentIndex<index:
					self.first = currentNode.nextPoint
					currentNode = currentNode.nextPoint 
					currentIndex+=1

				nextNode = self.first.nextPoint
				self.first.nextPoint = node 
				node.nextPoint = nextNode 
				self.first = firstNode 
			
			else:
				return -1

		except:
			return -1		


	def search(self,value):
		
		global globalIndex
		currentNode = self.first
		index= 1
		
		try:
			while value!= currentNode.value and index<=globalIndex:
				index+=1
				currentNode= currentNode.nextPoint
			return index
		except:
			return-1


	def update(self,index,value):
		
		global globalIndex
		
		firstNode = self.first
		currentNode = self.first
		currentIndex = 1

		try:	
			if index <=globalIndex:
				while currentIndex<index:
					self.first = currentNode.nextPoint
					currentNode = currentNode.nextPoint 
					currentIndex+=1
			else:
				return -1
			
			self.first.value = value
			self.first = firstNode
		
		except:
			return -1


	def deletionAll(self):
		self.first = None
		self.last = None
	

	def deletionFirstNode(self):
		global globalIndex
		
		try:
			if globalIndex ==1:
				self.first =None
				self.last= None 
			else:
				self.first = self.first.nextPoint
		
		except:
			return -1
		
		globalIndex-=1
			

	def deletionLastNode(self):
		global globalIndex
		
		try:
			if globalIndex== 1:
				self.first =None
				self.last= None
			
			else:
				index= 2
				currentNode = self.first
				
				while index<globalIndex: 
					currentNode = self.first.nextPoint
					index+=1
				
				self.last = currentNode
				self.last.nextPoint= None

		except:
			return -1
		
		globalIndex-=1

	
	def deletionNodeByIndex(self,deletionIndex): 
		global globalIndex
		
		if deletionIndex ==1:
			return "Warning:-Using deletionFirstNode() method in this case "
		
		elif deletionIndex == globalIndex:
			return "Warning: -Using deletionLastNode() method in this case"

		elif deletionIndex<1 or deletionIndex>globalIndex:
			return "Warning: -Index out of range"
		
		else:
			
			firstNode= self.first

			currentNode = self.first
			
			index = 2
			while index<deletionIndex:
				self.first = currentNode.nextPoint
				currentNode = currentNode.nextPoint
				index+=1
			
			self.first.nextPoint = self.first.nextPoint.nextPoint
			self.first = firstNode