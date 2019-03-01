def compute_first(actual,item):
	if item in term :
		first_[actual].add(item)
		return False
	temp = productions[item].split("|")
	for ele in temp:
		segments = ele.split(" ")
		segments = [x for x in segments if x !='']
		for i in range(len(segments)):
			if segments[i] in nonterm:
				ind = i
				while(compute_first(actual,segments[ind])):
					if ind+1<len(segments):
						ind = ind + 1
					else:
						first_[actual].add('e')
						break
						 
			else:
				if segments[i]=='e':
					if i==len(segments)-1:
						first_[actual].add('e')
					return True;
				first_[actual].add(segments[i])
			break

def compute_follow(it):
	for item in productions:
		temp = productions[item].split("|")
		for ele in temp:
			segments = ele.split(" ")
			segments = [x for x in segments if x!='']
			for i in range(len(segments)):
				if segments[i]==it and i+1<len(segments):
					fst = first_[segments[i+1]]
					follow_[it] = follow_[it].union(first_[segments[i+1]])
					index = i+1
					while 'e' in fst and index<len(segments):
						follow_[it] = follow_[it].union(first_[segments[index]])
						if index==len(segments)-1:
							follow_[it] = follow_[it].union(follow_[item])
							foldep[it].add(item)
						else:
							fst = first_[segments[index+1]]
						index = index + 1 
					if 'e' in follow_[it]:
						follow_[it].remove('e');
				elif segments[i]==it :
					follow_[it] = follow_[it].union(follow_[item])
					foldep[it].add(item)
			
n = int(raw_input("Enter the number of productions "))
productions = {}
term = set()
nonterm = set()
for i in range(n):
	tmp = raw_input()
	arr = tmp.split('->')
	arr[0]=arr[0].replace(" ","")
	productions[arr[0]]=arr[1]
	nonterm.add(arr[0])
start = raw_input("Enter the start symbol ")

for item in productions:
	temp = productions[item].split("|")
	for ele in temp:
		segments = ele.split(" ")
		for s in segments:
			fg=0
			for i in nonterm:
				if i==s:
					fg=1
			if fg==0:
				term.add(s)
term = [x for x in term if x!='']
nonterm = [x for x in nonterm if x!='']
print "terminals\n",term
print "non-terminals\n",nonterm
first_ = {}
follow_ = {}
foldep = {}

for item in term:
	first_[item]=item
for item in nonterm :
	first_[item]=set()
	follow_[item]=set()
	foldep[item] = set()
	
follow_[start].add('$');
for item in nonterm:
	compute_first(item,item)

for item in nonterm:
	compute_follow(item)
	for el in foldep[item]:
		follow_[item] = follow_[item].union(follow_[el])
for item in nonterm:
	for el in foldep[item]:
		follow_[item] = follow_[item].union(follow_[el])

for item in nonterm:	
	print item 
	print first_[item]
	print follow_[item]

"""
S -> A C B | C b b | B a
A -> d a | B C 
B -> g | e
C -> h | e

"""

