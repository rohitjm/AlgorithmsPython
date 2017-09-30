list = [6,1,87,5,34,7,9,4];

for i in range (len(list)):
  print("value of i",i)
  for j in range (i+1,len(list)):
    print("value of j",j)
    #print("list",list)
    if list[i] > list[j]:
      t = list[i]
      list[i] = list[j]
      list[j] = t
  print ("at end of loop:", list)      
print (list)      
      