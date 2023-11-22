import copy
arr = [6,6,6,6,6,6,6]
# arr = [8,43,2,44,5,66,-12,10,50,1]

def partition (arr : list , left : int, right : int):
    l = left
    r = right
    pivot = left

    while l < r:
        while arr[r] >= arr[pivot] and r>pivot:
            r -=1
        arr[r], arr[pivot] = arr[pivot],arr[r]
        pivot = copy.copy(r)
        while arr[l] < arr[pivot] and l<pivot :
            l +=1
        arr[l], arr[pivot] = arr[pivot],arr[l]
        pivot = copy.copy(l)
    return pivot
    

def QuickSort(arr : list , l : int, r : int ):
    if r-l > 0 :
        k = partition(arr,l,r)
        QuickSort(arr, l, k-1)
        QuickSort(arr, k+1, r)

QuickSort(arr,0,len(arr)-1)


print(arr) #[-12, 1, 2, 5, 8, 10, 43, 44, 50, 66]
