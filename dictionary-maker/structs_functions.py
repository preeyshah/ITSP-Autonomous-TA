#!/usr/bin/python/

class Dnode:
	"""dictionary node"""

	def modify(self , list):
		self.word = list[0]
		self.type = list[1]

	def __init__(self):
		self.word=""
		self.type=""
		self.next = [False]*26
		
def listify(str):
	whats_left = []
	for char in str:
		whats_left.append(char)
	return whats_left

def addto(dict , word , whats_left):
	#print([whats_left , dict])
	if (ord(whats_left[0]) <= ord('Z')):
		whats_left[0] = chr(ord (whats_left[0]) + ord('a') - ord('A'))
	if (dict[ord(whats_left[0]) - ord('a')] == False):
		if (len(whats_left)==1):
			dict[ord(whats_left[0]) - ord('a')] = Dnode()
			dict[ord(whats_left[0]) - ord('a')].modify(word)
			return
		else:
			dict[ord(whats_left[0]) - ord('a')] = Dnode()
			addto(dict[ord(whats_left[0]) - ord('a')].next , word , whats_left[1:])
			return

	elif (len(whats_left) == 1):
		dict[ord(whats_left[0]) - ord('a')].modify(word)
		return

	else:
		addto(dict[ord(whats_left[0]) - ord('a')].next , word , whats_left[1:])
		return

def find(dict,word):
	return finder(dict,listify(word))

def finder (dict , word):
	if (dict[ord(word[0]) - ord('a')] == False):
		return ""
	elif (len(word) == 1):
		return (dict[ord(word[0]) - ord('a')].type)
	else:
		return finder(dict[ord(word[0]) - ord('a')].next , word[1:])

if __name__=="__main__":
	file = open("dictionary.txt" , 'r')
	dictionary = ""

	for chunk in file:
		dictionary+=chunk
	
	dicti = [False]*26
	trial = ["abominable" , "adj"]
	listed=listify(trial[0])
	addto(dicti,trial,listed)
	addto(dicti , ["abominabl" , "lklkl"] , listify("abominabl"))
	a = find(dicti , "abominabl")
	print(a)