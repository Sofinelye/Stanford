def MergeSort(arr):
    #A= 1st array (n/2)
    #B=2nd array (n/2)
    #C= output array [length = n]
    n = len(arr)

    if n == 1:
        return arr
    else:
        m = n//2
        A=arr[:m]
        B=arr[m:]
        MergeSort(A)
        MergeSort(B)
        i = j = k = 0
###Merge
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                arr[k] = A[i]
                i+=1

            else:
                arr[k] = B[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(A):
            arr[k] = A[i]
            i+=1
            k+=1

        while j < len(B):
            arr[k] = B[j]
            j+=1
            k+=1

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7,12,100,1,1000,10000]
    print ("Given array is", end="\n")
    printList(arr)
    MergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
