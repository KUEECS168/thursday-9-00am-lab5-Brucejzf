'''
Author: Bruce Jiang
KUID 3179112
Date: Mar 11 2026
Lab: Lab1005B
Last modified: 2026/3/11
purpose: First lab exercise for lab05
'''

shopping_list = []

while True:
    print("1.) Add Item")
    print("2.) Check off item")
    print("3.) Print list")
    print("4.) Exit")

    a = int(input("Enter a choice:"))

    if a == 1:
        b = input("What will you add to the list?:")
        shopping_list.append(b)
        continue

    elif a == 2:
        c = int(input("Which item will you check off?:"))
        c += 1
        shopping_list.pop(c)
        continue


    elif a == 3:
        print("Here is your list:")
        for i in range(0,len(shopping_list)):
            print(shopping_list[i])
        continue
    
    elif a == 4:
        print("good bye")
        break