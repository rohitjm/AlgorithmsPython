
def create_phone_number(num):

    i = 0
    res = ""

    while i < len(num):
        if i == 0:
            res = res+'('
        if i == 3:
            res = res+') '
        if i == 6:
            res = res+'-'
        res = res+str(num[i])
        i+=1

    return res

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        
