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
	type = "Does not exsist"
	b = soup.select('.me')[0].getText()
	if ord(b[0])<=ord('Z') and ord(b[0])>=ord('A'):
		return "proper_noun"
	a = soup.select('.dbox-pg')
	if len(a) > 0:
		type = a[0].getText() #go through the source code and find out where the lyrics are stored.
	return type

def find(dict,word):
	offline_answer = finder(dict,listify(word))
	if offline_answer == "":
		return find_online(word)
	return offline_answer

def finder (dict , word):
	if (dict[ord(word[0]) - ord('a')] == False):
		return ""
	elif (len(word) == 1):
		return (dict[ord(word[0]) - ord('a')].type)
	else:
		return finder(dict[ord(word[0]) - ord('a')].next , word[1:])


	'''trial = ["abominable" , "adj"]
	listed=listify(trial[0])

	addto(dicti,trial,listed)
	addto(dicti , ["abominabl" , "lklkl"] , listify("abominabl"))
	a = find(dicti , "abominabl")
	print(a)'''

	   
####################################################################################################################



#print(dicti)

mainlist = []
ref=0

def allcaps(stri):
	if(stri==""):
		a=False
	
	else:
		a=True
		for c in stri:
			if((not c=='\r') and (not (ord(c) >= ord('A')) and (ord(c) <= ord('Z')) )):
				a=False

	return a

def partofspeech(stri):
	ref=len(stri)
	#print(ref)
	for i in range(ref):
		if(stri[i]=='.'):
			break

	#print(i)
	if i==ref-1:
		return "ditch"

	else:
		j=i
		while(stri[j] != ','):
			j=j-1

		return stri[j+2:i]


#print(partofspeech(" dejnkrbak , ejnrfkjbwkjrnfbw, ewfbnkjrfbekj, n., dfknerwjnweihrgbiwhrb"))

'''i=0

def extract(stri):

    while(not (stri[i] == '\n' and stri[i+1] == '\n' and stri[i+2] == '\n' and stri[i+3] == '\n')):
		diction = ''
		speech = ''

		while(not (stri[i-1] == '\n' and
			ord(stri[i]) <= ord('Z') and ord(stri[i]) >= ord('A') and ord(stri[i+1]) <= ord('Z') and ord(stri[i+1]) >= ord('A'))):
			i+=1

		j=i

		while(stri[j] != '\n'):

			j+=1

		diction = stri[i:j]

		k=j

		while(stri[k] != ','):
			k+=1

		l=k+2

		while(stri[l] != '.'):
			l+=1

		i=l

		speech = stri[(k+2):l'''

def makelist(lis):
	p=len(lis)
	a=''
	for i in range(p-2):
		#print(allcaps(lis[i+1]))
		if (lis[i]=='\r' and allcaps(lis[i+1])):
			q=partofspeech(lis[i+2])
			if q!="ditch":
			#a=list[lis[i+1],partofspeech(lis[i+2])]
				a=[lis[i+1],partofspeech(lis[i+2])]

			#print(list(lis[i+1],partofspeech(lis[i+2])))
				mainlist.append(a)




if __name__=="__main__":
	file = open("dictionary.txt" , 'r')
	dictionary = ""

	dicti = [False]*26

	for chunk in file:
		dictionary+=chunk
	dictionary=dictionary.split("\n")
	print("Building list...")
	#print(dictionary[0:5])
	#print(dictionary[0])
	#print(dictionary[0] == '\r')
	#print(dictionary[1])
	#print(allcaps(dictionary[1]))
	makelist(dictionary)
	print("List created!!!")
	
	#print(mainlist[3][0][:-1])
	print("Building tree...")

	for word in mainlist:
		word[0] = word[0][:-1]
		addto(dicti , word , listify(word[0]))
	print("Tree created!!!")

	file.close()
	file = open("output.txt" , 'w')
	for elem in mainlist:
		file.write(elem[0])
		file.write(" - ")
		file.write(elem[1])
		file.write("\n")
	while True:
		word = raw_input("Enter a word: ")
		print(find(dicti , word))
	#mm=mainlist
	#print(mainlist)
	#(dictionary)

	#for c in mainlist:
	#	addto(dicti,c,listify(c[0]))

	#print(mainlist)


	#print(mm)
	#print(allcaps("Defn: The act of abacinating. [R.]"))
