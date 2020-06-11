class num:
    def __init__(self,i):
        i = int(i)
        self.value = i
        self.count = 1
        if i%10000==0:
            self.key = i/10000
        elif i < 0:
            self.key=i//10000+1
        else:
            self.key=i//10000

class two_sum:
    X={} #number value, and object
    Y=[] #distinct number
    Z={} #number key, number value
    count = 0
    results={}
    def add_num(self,n):
        if n.value not in self.X:
            self.X[n.value]=n
        elif n.value in self.X:
            self.X[n.value].count +=1
    def two_sum(self):
        for x in self.X:
            if self.X[x].count==1:
                self.Y.append(x) #get distinct numbers stored in Y
                if self.X[x].key not in self.Z:
                    self.Z[self.X[x].key] = [] #set empty dict
        for y in self.Y:
            self.Z[self.X[y].key].append(self.X[y].value)
        for key1 in self.Z:
            if key1>0:
                continue
            for key2 in range(int(-key1-1),int(-key1+2)):
                if key2 in self.Z:
                    values_1 =self.Z[key1]
                    values_2=self.Z[key2]
                    for v1 in values_1:
                        for v2 in values_2:
                            if v1==v2:
                                continue
                            values_sum = v1+v2
                            if abs(values_sum)<=10000 and values_sum not in self.results.keys():
                                self.count+=1
                                self.results[values_sum] = [v1,v2]

    def print_result(self):
        print(self.count)

s = two_sum()
with open('2sum.txt') as f:
    for i in f:
        number=num(i)
        #print(number)
        s.add_num(number)
s.two_sum()
s.print_result()
