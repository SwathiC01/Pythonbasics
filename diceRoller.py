from random import randint

num=int(input("How many dice would you like to roll: "))
l=[]
for i in range(num):
    dice_roll_num=randint(1,6)
    l.append(dice_roll_num)
print(l)