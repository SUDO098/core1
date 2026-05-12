def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if(arr[j]<arr[min_idx]):
                min_idx=j

        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

arr=[23,1,45,56,22,9]
print(arr)
print(selection_sort(arr))


#tc =O(n^2)
#sc=O(1)
