
# lent = int(input())
import random

list = []
# for i in range(1000): list.append(int(input()))
for i in range(1): list.append(random.randint(1,10**11))
print(list)
# b = 0
for i in list:
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 13 == 0 or i % 11 == 0:
        print("true", i)
    # elif i % 3 ==0:
        # print("true", i)
        # a = 1
    # elif i % 5 ==0:
    #     # print("true", i)
    #     a = 1
    # elif i == 1 or:
    #     a = 1
    # elif i == 17:
    #     a = 1
    # else:
    #     print("пиздец", i)
    #     b +=1
# print(b)
