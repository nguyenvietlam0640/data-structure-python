







class createArr():
	def __init__(self):
		
		self.count= None
		self.list = []
		return 


	
	def addList(self,value):
		
		currentIndex = self.count
		
		if currentIndex ==None:
			self.list.append(value)
			self.count = 0
		
		else:
			self.list.append(value)
			self.count+=1

	

	def showList(self):
		
		List = None
		currentIndex = self.count
		index = currentIndex
		
		while currentIndex != None and 0<=index<len(self.list):

			if List == None:
				List = str(self.list[currentIndex-index])
			
			else:
				List +=" "+ str(self.list[currentIndex-index])
			index-=1
		
		print("["+str(List)+"]")