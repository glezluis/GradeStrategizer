import slate 
import re
import os

class category:
  ''' A category for assignments with a weight towards total grade '''
  def __init__(self, title, weight):
    self.components = []
    self.title = title
    self.weight = weight
 
  def get_avg(self):
    score_sum = 0.0
    num_scores = 0

    for component in self.components:
      score_sum += component.score
      num_scores += 1 

    return score_sum / num_scores

def pdfScanner(fileName):
	catStrList = []
	perStrList = []
	categoryList = []

	with open(fileName) as f: 
		doc = slate.PDF(open(fileName))


	allcatsNotfound = True

	catStr = ""
	percentStr = ""

	allcatsRE = re.compile(r'Category.*Grade(.*)',re.DOTALL) 
	singlecatRE = re.compile(r'(\w+[/][\-\w]+|\w+[/]|\w+ \w*|[a-zA-z]+)')
	percentRE = re.compile(r'(\d+)%')
	i = 0;

	while i < len(doc) and allcatsNotfound :
		page = doc[i]
		wholematch = re.search(allcatsRE, page)
		if wholematch:
			info = wholematch.group(1)
			#print info
			for line in info.split('\n'):
				catMatch = re.match(singlecatRE, line)
				
				percentMatch = re.match(percentRE, line)
					
				if percentMatch:
					perStrList.append(percentMatch.group(1))
					allcatsNotfound = False

				elif catMatch and  allcatsNotfound :
					# print catMatch.groups()
					catStrList.append(catMatch.group(1))
		i+=1

	slashMatchRE = re.compile(r'(\w+[/])')
	listSize = len(catStrList)
	i = 1
	if len(catStrList) != len(perStrList):
		while i < listSize:
		 	slashMatch = re.match(slashMatchRE, catStrList[i-1])
		 	if slashMatch:
		 		catStrList[i-1] = catStrList[i-1] +' ' + catStrList[i]
		 		catStrList.remove(catStrList[i])
		 		listSize = len(catStrList)
		 	if (catStrList[i] == "Assignments" or 
			(catStrList[i] == "Activities")):
		 		catStrList[i-1] = catStrList[i-1] +' ' + catStrList[i]
		 		catStrList.remove(catStrList[i])
		 		listSize = len(catStrList)
		 	i+=1
	#print catStrList, perStrList
	print "The categories are: "
	if len(catStrList) == len(perStrList):
		for i in range(len(catStrList)):
			categoryList.append(category(catStrList[i],perStrList[i]))
			print categoryList[i].title, categoryList[i].weight+'%'

# print '\n', "Ethics CS315"
# pdfScanner("ethicsSyll.pdf")

print '\n',  "Algorithms CS335:"
pdfScanner("algsyll.pdf")

print '\n', "Software Engineering CS363:"
pdfScanner("syll.pdf")
