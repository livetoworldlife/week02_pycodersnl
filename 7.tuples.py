# 7.1 - Convert a tuple to a string and print.
tup1 = ('n', 'e', 't', 'h', 'e', 'r', 'l', 'a', 'n', 'd', 's')
a = ''
for i in tup1:
    a=a+i
print(a)

#"netherlands"

# 7.2 - unzip a list of tuples into individual lists and print.
tup2 = [(3, 6), (5, 8), (7, 4)]
a, b = [], []
for i in range(len(tup2)):
    a.append(tup2[i][0])
    b.append(tup2[i][1])
c = [tuple(a) , tuple(b)]
print(c)


#[(3, 5, 7), (6, 8, 4)]

# 7.3 -  convert a list of tuples into a dictionary and print.
tup3 = [("a", 1), ("a", 2), ("a", 3), ("b", 1), ("b", 2), ("c", 1)]

d = {}
for x, y in tup3:
    d.setdefault(x, []).append(y)
print(d)
#{'b': [1, 2], 'c': [1], 'a': [1, 2, 3]}



# ############################################################# The End 
