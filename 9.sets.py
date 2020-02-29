# 9.1 Create an intersection of sets and print it.
data1 = (["green", "blue"])
data2 = (["blue", "yellow"])

    # convert the lists to the sets
data1_set = set(data1)
data2_set = set(data2)
    # intersection of these sets
int_set = data1_set.intersection(data2_set)
    # and print it.
print(int_set)
    # or easy way
print(set(data1) & set(data2))



# 9.2 Create set difference and print them.
data3 = (["apple", "mango"])
data4 = (["mango", "orange"])

    # convert the lists to the sets
data3_set = set(data3)
data4_set = set(data4)
    # difference of these sets
dif_set = data3_set.difference(data4_set)
    # and print it.
print(dif_set)
    # or easy way
print(set(data4) - set(data3))



# 9.3 Find maximum and the minimum value in a set and print them.
data5 = ([5, 10, 3, 15, 2, 20])

    # convert the list to the set
data5_set = set(data5)
    #print max value and min value

max_data5 = None
min_data5 = None
for i in data5_set:
    if max_data5 is None or i > max_data5:
        max_data5 = i
    if min_data5 is None or i < min_data5:
        min_data5 = i
print('The max value is :', max_data5)
print('The min value is :', min_data5)

# ############################################################# The End 

