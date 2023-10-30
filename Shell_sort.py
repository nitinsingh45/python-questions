#Shell sort implementation in python

def shell(arr):
    n = len(arr)
    g= n//2
    while g>0:
        for i in range(g,n):
            m = arr[i]
            j = i
            while j >= g and arr[j-g]>m:
                arr[j] = arr[j-g]
                j -= g
            arr[j]=m
        g = g // 2
    return arr


#input the array
arr=list(map(int, input("elements of array:-").strip().split()))

#sort the array
shell(arr)

#print the sorted array
print ("Array after implementation of shell sort is:")
for i in range(len(arr)):
   print (arr[i])

