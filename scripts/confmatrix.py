#takes two files, one classified by you the other classified by the classifier, creates confusion matrix of errors

import numpy

class ConfusionMatrix(object):

	


	def __init__(self):

		self.tags=["PERS","ORG","LOC", "0"]
		self.sumMatrix=0

	def create(self):

		array1,array2 = self.arrays('file1.txt','file2.txt')

		ConfMatrix=self.sort(array1,array2)

		

		self.Mprint(ConfMatrix)
		

	def Mprint(self,ConfMatrix):
		#Prints two dimensional array as matrix of percentages


		PrintConf=[]

		header=['Act/Try']+self.tags
		PrintConf.append(header)

		for i in range(0,len(self.tags)):
			row=[]
			row.append(self.tags[i])
			for x in ConfMatrix[i]:
				val=x/float(self.sumMatrix)*100
				row.append(val) 
			PrintConf.append(row)

		Accuracy,Persion,Recall=self.scores(ConfMatrix)


		print('\n'.join(['\t'.join(['{:4}'.format(item) for item in row]) 
			for row in PrintConf]))

	def sort(self,array1,array2):
		#Sorts the two arrays into a two dimensional array recording the nummer
		#of each kind of training/test combination
		n1=len(array1)
		n2=len(array2)
		assert n1==n2
		matrix = [ [ 0 for i in range(len(self.tags)) ] for j in range(len(self.tags)) ]

		for i in range(0,n1):
			self.sumMatrix+=1
			k=self.tags.index(array1[i])
			j=self.tags.index(array2[i])
			matrix[j][k]+=1
		
		print self.sumMatrix
		return matrix



	def scores(self,ConfMatrix):
		#Caclulates scores 
		#Accuracy(tp+tn)/tp+tn+fp+fn
		#Percision: tp/tp+fp
		#Recall: tp/tp+fn

		TruePos=0
		FalsePos=0
		FalseNeg=0
		TrueNeg=ConfMatrix[len(ConfMatrix),len(ConfMatrix)]
		for x in range(0,len(ConfMatrix)-1):
			TruePos+=ConfMatrix[x][x]
			FalseNeg+=ConfMatrix[len(ConfMatrix][x]
		


		f=1
		return f,f,f

	def arrays(self,file1,file2):
		#creates two arrays containing the tag of every line in the two documents
		array1 = []
		array2 = []
		with open(file1, 'r') as training, open(file2, 'r') as test:
			for line in training:
				s=line.split('\t')
				sline=s[1].rstrip()
				array1.append(sline)
			
			for line in test:
				n=line.split('\t')
				nline=n[1].rstrip()
				array2.append(nline)
		return array1,array2

ConfusionMatrix().create()