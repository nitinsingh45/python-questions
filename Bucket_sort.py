#Bucket sort implementation in python

def insert(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while (j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp

def bucket_sort(arr):
    largest = max(arr)
    length = len(arr)
    size = largest/length
 
    bucket = [[] for _ in range(length)]
    for i in range(length):
        j = int(arr[i]/size)
        
        if j != length:
            bucket[j].append(arr[i])
        else:
            bucket[length - 1].append(arr[i])
 
    for i in range(length):
        insert(bucket[i])
 
    res = []
    
    for i in range(length):
        res = res + bucket[i]
 
    return res
 
arr=list(map(int, input("elements of array:-").strip().split()))

#sort the array
sorted_list = bucket_sort(arr)

#print the sorted array
print ("Array after implementation of bucket sort is:",end='')
print(sorted_list)
