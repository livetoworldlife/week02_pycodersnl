

use_list = []
use_items = ''
number = int()

# Enter the list items until q
while use_items != 'q':
    use_items = input("Enter the list items as a number: (to stop the program please enter 'q'): ")
    if use_items != 'q':
        use_list.append(int(use_items))
    else:
        use_list.sort()
        break

# Enter Xth smallest number but control if the number you enter is greater than the length of the list
wh_kont = True
while wh_kont:
    x = int(input("Which number do you want to know as Xth smallest number in the list? "))
    if x <= len(use_list):
        number = use_list[x - 1]
        print("{}. smallest element in the given list is {}.".format(x, number))
        wh_kont = False
    else:
        print("the number you enter is greater than the length of the list"
              "\n")
        continue



# ############################################################# The End 
