

# Create ten character of English alphabet(from "a" to "j")
keys_list = []
keys_list = [chr(x) for x in range(ord('a'), ord('j')+1)]

# Create a tuple from 0-10 for "a" , 11-20 for "b" and so on respectively
value_list = []
a, b = 0, 1
for i in range(0,len(keys_list)):
    items_tuple = (int(y) for y in range(a*1,b*10))
    value_list.append(tuple(items_tuple))
    a += 10
    b += 1

# Add keys and values to a dictionary
word_intervals = {keys_list[j] : value_list[j] for j in range(0,len(keys_list))}
print(word_intervals)


# ############################################################# The End 
