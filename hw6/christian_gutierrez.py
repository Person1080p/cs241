#Christian Gutierrez SP22
#took me like an hour to remember how 2 do python stuff again, and #2 needed a lot of thinking
def isPhoneNumber(string):
    if len(string) != 10:
        return False
    for i in range(0,10):
        if string[i] not in "0123456789":
            return False
    return True
#print(isPhoneNumber("1234367890"))
def validBlock(arr,a,b,c):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            for k in range(0,len(arr)):
                if ((i==j+1 or i==j-1) and (arr[i]<=a and arr[j]<=b and arr[k]<=c)and(i!=j and j!=k and i!=k)):
                    #print(arr[i] ,arr[j],arr[k])
                    return True
    return False
#print(validBlock([1,2,3,4,5], 4, 4, 1) )
def divisibleSum(arr,num):
    for i in range(len(arr)):
        if i+1 >= len(arr):
            return False
        if (arr[i]*arr[i+1]) % num == 0:
            return True
    return False
#print(divisibleSum([1,2,3,4], 11) )