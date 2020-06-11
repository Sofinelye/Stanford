
def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        m = len(arr)//2
        a = arr[:m]
        b = arr[m:]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = arr
        i = j = k=0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k]=b[j]
            j += 1
            inversions += (len(a)-i)
        k+=1

    while i<len(a):
        c[k]=a[i]
        i+=1
        k+=1
    while j<len(b):
        c[k]=b[j]
        j+=1
        k+=1
    return c, inversions

if __name__ == '__main__':
    file = open("input_inversion.txt",'r')
    lines = file.read().split('\n')
    file.close()
    arr = []
    for a in lines:
        if a != '':
            a = int(a)
            arr+=[a]
    #print(arr)

    print ("Inversion Count is:", end="\n")
    print(mergeSortInversions(arr)[1])
