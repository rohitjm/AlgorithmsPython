
def find_even_index(arr):

    # from left to right check the sums of the nums to the right and left of
    # the current index

    if len(arr) % 2 == 0:
        return -1

    r_tot = 0
    l_tot = 0

    for x in range(1, len(arr)):
        # print arr[x]
        # print(x)
        r_tot += arr[x]

    if r_tot == l_tot:
        return 0

    print("r_tot: "+str(r_tot))
    index = 1

    while index != len(arr):
        r_tot -= arr[index]
        l_tot += arr[index-1]

        # print(l_tot)
        # print(r_tot)

        if l_tot == r_tot:
            return index

        index += 1

    return -1


print(find_even_index([1,2,1]))
print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([20,10,30,10,10,15,35]))
print(find_even_index([10,-80,10,10,15,35,20]))
