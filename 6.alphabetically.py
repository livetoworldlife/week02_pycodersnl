# Sort the dictionary data values below.
data = {'a':[5, 3, 9, 0, 2, 3, 1],'b':[4, 7, 5, 1, 2],'c':[8,1, 3, 2, 4]}
    #sorting 1
sorted_d = sorted(i for i in data.values())
print(sorted_d)

    #sorting 2
a,b,c=[],[],[]
x=0
while x < len(data):
    for s in sorted(data):
        x = x + 1
        if x == 1:
            a = data[s]
        if x == 2:
            b = data[s]
        if x == 3:
            c = data[s]
a.sort()
b.sort()
c.sort()
print(a,"\n",b,"\n",c)


    #sorting 3
for i, j in data.items():
    sorted_da = {i: sorted(j)}
    print(sorted_da)


# ############################################################# The End 
