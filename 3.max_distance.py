

inp_list = []
use_items = ''
maximum_repeated_number = int()
distance = 0
mp_dic = {}

# Enter the list items until q
while use_items != 'q':
    use_items = input("Enter the list items as a number: (to stop the program please enter 'q'): ")
    if use_items != 'q':
        inp_list.append(int(use_items))
    else:
        break

# list items is a key for map dictionary. If the item is not in key, index of list items will add in values
for i in range(len(inp_list)):
    if inp_list[i] not in mp_dic.keys():
        mp_dic[inp_list[i]] = i
    else: # If the repeated item is in key, the distance can be calculated also the max number can be found
        distance = i - mp_dic[inp_list[i]]
        maximum_repeated_number = inp_list[i]

print("Max Distance between the maximum repeated number ({}) is: {}".format(maximum_repeated_number, distance))


# ############################################################# The End 
