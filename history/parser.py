#!/usr/bin/python/


def addinfo(node,text):

	split_text = []


	current_text = ""

	for element in text:
		if subtopic(element) or topic(element):
			break
		else :
			last = element[-1:]
			if (last in paragraph_terminators) or ( ord(last) > 127 ):
				current_text += element
				split_text.append(current_text)
				current_text = ""
			else:
				current_text += element
				current_text += " "
	
	for elem in split_text:
		if fig(elem) :
			pass
		elif (len(elem.split())<20):
			pass
		elif (ord(elem[1])>64) and (ord(elem[1])<97):
			pass
		else:
			child_node = Node()
			child_node.add_keyword(elem)
			makepara(child_node,elem)
			node.add_child(child_node)

def singledigit(elem):
	if (ord(elem[0])>48) and (ord(elem[0])<57) and (elem[1]==" ") and (elem[2]=="-") :
		return True
	else :
		return False

def doubledigit(elem):
	if (ord(elem[0])>48) and (ord(elem[0])<57) and (ord(elem[1])>48) and (ord(elem[1])<57) and (elem[2]==" ") and (elem[3]=="-"):
		return True
	else :
		return False


def makepara(node,para):
	p = para.split(".")
	for e in p:
		l =Leaf()
		if (e[-3:]=="Fig"):
			e=e[:-3]
		elif singledigit(elem) or doubledigit(elem):
			continue 
		elif (len(e.split()) <= 3):
			continue
		l.add_sentence([e])	
		node.add_child(l)


def topic(elem):
	if (ord(elem[0])>48)and (ord(elem[0])<57) and (elem[1]==" "):
		return True
	else :
		return False


def subtopic(elemnt):
	x = ord(elemnt[0])
	if (x>48)and(x<57) and (elemnt[1]==".") and (ord(elemnt[2])>48) and (ord(elemnt[2])<57) and (elemnt[3]==" "):
		return 	True
	else :
		return False

def fig(element):
	if (element[0]=="F")and(element[1]=="i")and (element[2]=="g") :
		return True
	else :
		return False

class Node:
	"""Topic"""

	def __init__(self):
		self.children = []
		self.keywords = []

	def print_node(self , i):
		indent = " "*i
		print(indent + self.keywords[0])
		for elem in self.children:
			elem.print_node(i+4) 

	def add_keyword(self , kword):
		self.keywords.append(kword)

	def add_child (self , chld):
		self.children.append(chld)

class Leaf:
	"""Leaf"""

	def __init__(self):
		self.keywords = []
		self.sentence = []

	def add_keyword(self , kword):
		self.keywords.append(kword)

	def add_sentence (self , words):
		for word in words:
			self.sentence.append(word)

	def print_node(self, i):
		indent = " "*i
		print(indent+self.sentence[0])

paragraph_terminators = {"." , "!" , "?" , "'"}

if __name__ == "__main__":
	file = open("chapter1.txt" , 'r')
	text = ""
	for chunk in file:
		text += chunk

	text = text.split("\n")

	mother_node = Node()
	mother_node.add_keyword("Rise of Nationalism in Europe")

	text = [x for x in text if len(x) >= 4]
	out_file = open("output.txt" , 'w')
	for elem in text:
		out_file.write("\n")
		out_file.write("\n")
		out_file.write(elem)	

	for x in range(len(text)) :
		element = text[x]
		y = ord(element[0])
		if (y > 48) and (y < 58) :
			if (element[1]==" ") :
				if (len(mother_node.children)<y-48):
					child_node = Node()
					child_node.add_keyword(element[2:])
					addinfo(child_node,text[x+1:])

					mother_node.add_child(child_node)
				else:
					mother_node.children[y-49].add_keyword(element[2:])
			elif (element[1]=="."):
				z = ord(element[2])
				if (z > 48) and (z < 58) :
					if (element[3]==" "):
						child_node = Node()
						child_node.add_keyword(element[4:])
						addinfo(child_node,text[x+1:])
						if (len(mother_node.children)<y-48):
							children_node = Node()
							mother_node.add_child(children_node)
						else:
							mother_node.children[y-49].add_child(child_node)






	mother_node.print_node(0)

	'''			
	split_text = []


	current_text = ""

	for element in text:
		last = element[-1:]
		if (last in paragraph_terminators) or ( ord(last) > 127 ):
			current_text += element
			split_text.append(current_text)
			current_text = ""
		else:
			current_text += element
			current_text += " "

	out_file = open("output.txt" , 'w')

	#split_text = [x for x in split_text if len(x.split()) > 20]

	for elem in split_text:
		out_file.write("\n")
		out_file.write("\n")
		out_file.write(elem)'''
