# lent = int(input())
# list = input().split()
# list = [int(item) for item in input().split()]
lent = 10
list = [int(item) for item in "6 8 4 6 7 1 6 3 4 5".split()]
not_in_list = []

for i in range(lent):
    if list.count(i + 1) == 0: not_in_list.append(i + 1)
print(not_in_list)

for i in range(lent):
    if list.count(list[i]) > 1 and list[i] > 0:
        num = list[i]
        for a in range(list.count(list[i])):
            list[list.index(num)] = num - (num * 2)

for i in range(len(list)):
    if i < 0:
        abss = abs(i)
        if abss == i + 1:
            print(abss)
        # else:
#             abss = abs(num - (ind + 1))
#             # print("мод",abss)
#             if min > abss:
#                 min = abss
#                 ind_f = ind
#             # print("min",min)
#             list[ind] = 0
#         list[ind_f] = num
# print(list)
# for i in range(1, len(list)+1):
#     if list.count(i) == 0:
#         list[list.index(0)] = i

print(list)

# 6 8 4 6 7 1 6 3 4 5 изначально
# [2, 8, 4, 9, 7, 1, 6, 3, 10, 5] мое
# 2 8 4 6 7 1 9 3 10 5  как должно быть


# if list.count(list[i]) > 1 and list[i] < 0:
    # num = list[i]
    # min = len(list)
    # ind_f = 0
    # print(min)
    # for a in range(list.count(list[i])):
    #     ind = list.index(num)
    #     abss = abs(num - (ind + 1))
    #     # print("мод",abss)
    #     if min > abss:
    #         min = abss
    #         ind_f = ind
    #     # print("min",min)
    #     list[ind] = 0
    # list[ind_f] = num
# print(list)
# for i in range(1, len(list)+1):
#     if list.count(i) == 0:
#         list[list.index(0)] = i





# Пожар
# time, time_end, price, coef = [],[],[],[]
# for i in range(int(input())):
#     a,b,c = input().split()
#     time.append(int(a))
#     time_end.append(int(b))
#     price.append(int(c))
#     coef.append(price[i] / time[i])
#
# print(time,time_end,price, coef)
# coef_range = []
# for i in range(len(coef)):
#     coef_range.append(coef.index(max(coef)))
#     coef[coef_range[-1]] = 0
# print(coef_range)
#
# sum_price, time_now, item, items = 0, 0, 0, ""
# for i in coef_range:
#     if time[i] >= time_end[i]: continue
#     elif time_end[i] > time_now + time[i]:
#         time_now += time[i]
#         sum_price += price[i]
#         item += 1
#         items += ' ' + str(i + 1)
#
# print(sum_price)
# print(item)
# print(items.replace(" ", "", 1))