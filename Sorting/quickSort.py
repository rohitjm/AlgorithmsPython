# Quicksort implementation in Python

def quickSort(nums, start, end):
  if start < end:
    par = partition(nums, start, end)

    quickSort(nums, par, end)
    quickSort(nums, start, par-1)



def partition(nums, start, end):
  
  high = nums[end]
  lowPos = start -1

  for j in range(start, end):
    if nums[j] <= high:
      nums[j],nums[lowPos] = nums[Pos],nums[j]

  nums[end],nums[lowPos+1] = nums[lowPos+1],nums[end]
  return lowPos+1


myArr = [8,4,3,6,4,2,8,6]
print(myArr)
quickSort(myArr,0,len(myArr))
print(myArr)
  
