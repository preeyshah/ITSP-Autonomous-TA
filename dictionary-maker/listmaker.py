mainlist = []
ref=0

def allcaps(stri):
	if(stri==""):
		a=False
	
	else:
		a=True
		for c in stri:
			if(not (ord(c)<=ord('Z') and ord(c)>=ord('A'))):
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


print(partofspeech(" dejnkrbak , ejnrfkjbwkjrnfbw, ewfbnkjrfbekj, n., dfknerwjnweihrgbiwhrb"))

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
		if (lis[i]=='' and allcaps(lis[i+1])):
			print(i)
			q=partofspeech(lis[i+2])
			if q!="ditch":
			#a=list[lis[i+1],partofspeech(lis[i+2])]
				a=[lis[i+1],partofspeech(lis[i+2])]

			#print(list(lis[i+1],partofspeech(lis[i+2])))
				mainlist.append(a)




if __name__=="__main__":
	file = open("dicts.txt" , 'r')
	dictionary = ""

	for chunk in file:
		dictionary+=chunk
	dictionary=dictionary.split("\n")
	makelist(dictionary)
	print(mainlist)
	#mm=mainlist
	#print(dictionary)
	#(dictionary)
	#print(mm)
	#print(allcaps("Defn: The act of abacinating. [R.]"))
