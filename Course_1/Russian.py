def Russian(x,y):
    if x == 0:
        return 0
    if x % 2 ==0:
        return 2*Russian(x/2,y)
    if x % 2 ==1:
        return 2*Russian((x-1)/2,y)+y
output = Russian(1934823579570985702984759823745084275349,2342837348754096870470487651232343453)
print(output)
