def listfunc(list):
	#print(list)
	#print('Length of list is: '+ str(len(list[0])))
	for i in range(len(list[0])):
		for j in range(len(list)):
			print(list[j][i])

spam=[[1, 2, 3],
      [4, 5]]
listfunc(spam)
