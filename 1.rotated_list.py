

# First line of input
ind_slp = int(input("How many index you will slip left the whole data in the list? "))
list_elements, left_list, right_list, use_items = [], [], [],''

# Second line of the data
while use_items != 'q':
    use_items = input("Enter the list items which you will rotate : (to stop the program please enter 'q'): ")
    if use_items != 'q':
        list_elements.append(use_items)
    else:
        break

# left part of the list is 0 to slip index
for i in range(0,ind_slp):
    left_list.append(list_elements[i])

# right part of the list is slip index to last items
for j in range(ind_slp,len(list_elements)):
    right_list.append(list_elements[j])

# to rotate the list
list_elements = right_list + left_list

print("The new order of list is:", list_elements)

# Or easy way
list_elements = (list_elements[-ind_slp:] + list_elements[:-ind_slp])
print("The new order of list is:", list_elements)

# ############################################################# The End 
