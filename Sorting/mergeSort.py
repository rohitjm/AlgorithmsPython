list = [6,1,87,5,34,7,9,4];

def mergeSort(start, end, list):

  if(start>=end):
  	return
  else:	
  	#find midpoint for the start and end
  	mid = (start+end)/2
  	return merge(mergeSort(start, mid, list), mergeSort(mid+1, end, list))  
  


def merge(listA, listB):

  aWalker = 0
  bWalker = 0
  resWalker = 0
  res = []

  while aWalker < len(listA) and bWalker < len(listB):
  	print(resWalker)	

  	if listA[aWalker] < listB[bWalker]:
  		res[resWalker] = listA[aWalker]
  		aWalker+=1
  		resWalker+=1
  	else:
  		res[resWalker] = listB[bWalker]
  		bWalker+=1
  		resWalker+=1

  	
  

  while aWalker < len(listA):
  	res[resWalker] = listA[aWalker]
  	resWalker+=1
  	aWalker+=1

  while bWalker < len(listB):
  	res[resWalker] = listB[bWalker]
  	resWalker+=1
  	bWalker+=1

  return res		


print(merge([2,4,9],[1,5,10]))

# mergeSort(0, len(list)-1, list)
