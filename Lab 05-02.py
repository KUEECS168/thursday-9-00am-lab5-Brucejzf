'''
Author: Bruce Jiang
KUID 3179112
Date: Mar 11 2026
Lab: Lab1005B
Last modified: 2026/3/11
purpose: Second lab exercise for lab05
'''

mission_list = []

while True:
    a = input("Enter planet name:")
    mission_list.append(a)
    b = input("Is the mission over?(y/n)").lower()
    if b == "n":
        continue
    elif b == "y":
        c = input("which planet do you want the neighbors for?:")
        d = mission_list.index(c)
        e = d + 1
        f = d - 1
        print(f'Planets neighboring {c}:')
        print(" "*4 + mission_list[e])
        print(" "*4 + mission_list[f])
        print('Program ending...')
        break