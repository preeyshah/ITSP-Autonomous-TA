#!/usr/bin/python/
import bs4 #to parse from the html code
import requests #to get the html code

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
	if not ( ord(whats_left[0])<=ord('z') and ord(whats_left[0])>=ord('a') ):
		return 
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

def find_online(word):
	base = "http://www.dictionary.com/browse/"
	link = base+word
	html_response = requests.get (link)
	html_code = ""
	for chunk in html_response.iter_content (100000):
		html_code+=chunk
	soup = bs4.BeautifulSoup(html_code , "lxml") #make a bs4 object of the code
	type = "Does not exist"
	a = soup.select('.me')
	if len(a) == 0:
		return type
	b = a[0].getText()
	if ord(b[0])<=ord('Z') and ord(b[0])>=ord('A'):
		return "proper_noun"
	a = soup.select('.dbox-pg')
	if len(a) > 0:
		type = a[0].getText() #go through the source code and find out where the lyrics are stored.
	return str(type)

def check_else_find(dict,word):
	offline_answer = finder(dict,listify(word))
	if offline_answer == "":
		ans = find_online(word)
		addto(dict,[word , ans] , listify(word))
		return [word , ans]
	print("already there in dictionary: " + offline_answer)
	return "0"

def finder (dict , word):
	if (dict[ord(word[0]) - ord('a')] == False):
		return ""
	elif (len(word) == 1):
		return (dict[ord(word[0]) - ord('a')].type)
	else:
		return finder(dict[ord(word[0]) - ord('a')].next , word[1:])

def regularise(string):
	splitters = ['.' , ',' , ':', ';', '!' , '?', '(',')','[',']','{','}','-' , '$','/',"'"]
	for splitter in splitters:
		string = string.replace(splitter , " ")
	for i in range(128,256):
		string = string.replace(chr(i) , " ")
	for i in range(10):
		string = string.replace(chr(i+48) , "")
	return [x for x in string.split() if len(x)>1]

def convert_to_small(string):
	ans=""
	for character in string:
		if ord(character) <= ord('Z') and ord(character)>=ord('A'):
			ans += chr( ord(character) + 32 )
		else:
			ans+=character
	return ans

def is_number(string):
	character = string[0]
	if ord(character)<=ord('9') and ord(character)>=ord('0'):
		return True
	else:
		return False

def add_to_dictionary(string):
	words = string.split("/")[:-1]
	for word in words:
		a = word.split("-")
		addto(dict , a , listify(a[0]))

dict = [False]*26

if __name__=="__main__":
	input1 = open("input2.txt" , 'r')
	dic_yet = ""
	print("Building dictionary")
	for chunk in input1:
		dic_yet+=chunk
	add_to_dictionary(dic_yet)
	print("Done")
	input = open("book2.txt" , 'r')
	output = open("output.txt" , 'w')
	input_set = ""
	for chunk in input:
		input_set+=chunk
	temp = regularise(input_set)
	text=[]
	for element in temp:
		text.append(convert_to_small(element))
	training_set = [x for x in text if not is_number(x)]
	count = len(dic_yet.split("/"))
	print(count)
	for word in training_set:
		a = check_else_find(dict , word)
		if not a == "0":
			output.write(a[0])
			output.write("-")
			output.write(a[1])
			output.write("/")
			count += 1
			print(str(count) + ". " + a[0] + " - " + a[1])