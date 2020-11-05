# переворачивать риснуки
# def turn(num_figure, count_turn):
#     list_work = []
#     str = ""
#     for i in range(num_figure, num_figure + item_char): list_work.append(list[i])
#     for a in range(count_turn):
#         # print("это a",a)
#         for i in range(item_char):
#             for c in range(len(list_work) - 1, -1, -1):
#                 str += list_work[c][i]
#         list_work.clear()
#         list_work = [str[i:i + item_char] for i in range(0, len(str), item_char)]
#         # print("list",list_work, a)
#         str = ''
#     return list_work
#
# def horizontal(num_figure):
#     list_work = []
#     for i in range(num_figure, num_figure + item_char): list_work.append(list[i])
#     for a in range(item_char):
#         # print("before",list_work)
#         list_work[a] = list_work[a][::-1]
#         # print("after",list_work)
#     return list_work
#
# def vertical(num_figure):
#     list_work = []
#     for i in range(num_figure, num_figure + item_char): list_work.append(list[i])
#     return list_work[::-1]
#
# v = input().split()
# count_item, item_char = int(v[0]), int(v[1])
# list = []
# for i in range(count_item * item_char):
#     list.append(input())
#
# v = input().split()
# actions, lines = int(v[0]), int(v[1])
# str = ""
# for i in range(lines):
#     str +=input() + " "
# list_command = str.split()
#
# # print(list, list_command)
#
# list_output = []
# for command in list_command:
#     num_item, num_com = command.split(":")
#     num_com, num_item = int(num_com), int(num_item)
#     figure_number = num_item * item_char
#     if 0 <= num_com <= 3:
#         list_output.append(turn(figure_number, num_com))
#         # print(num_com)
#     elif num_com == 4:
#         list_output.append(horizontal(figure_number))
#         # print(4)
#     elif num_com == 5:
#         list_output.append(vertical(figure_number))
#         # print(5)
#         # print("ok", vertical(figure_number))
#
# # print(list_output)
# before = 0
# for line in range(lines):
#     for i in range(item_char):
#         for char in range(actions):
#             print(list_output[char][i], end="")
#         print()
#     for a in range(actions):
#         list_output.remove(list_output[0])
#         # print(list_output)
#     # actions +=actions
#     # before += actions




# что то там зум про центр масс
# count = int(input())
# x_final, y_final, m_final = 0.0, 0.0, 0
# for i in range(count):
#     x,y,m = input().split()
#     x_final += int(x) * int(m)
#     y_final += int(y) * int(m)
#     m_final += int(m)
# print(x_final/m_final,y_final/m_final)



# Автобус
# value = input().split()
# # finish, tank, azs, count = int(value[0]), int(value[1]), int(value[2]), int(value[3])
# finish, tank, azs, count = 1000000, 1, 999999, 1
# before_azs = (finish - azs) * 2 if count > 1 else (finish - azs), finish * 2 - ((finish - azs) * 2)
# # print(before_azs)
# tank_now = tank - azs
# if tank_now < 0:
#     print(-1)
#     exit()
# # print(tank_now)
# lent = (finish * count) - azs
# values, binar = 0, 0
# while lent > 0:
#     # print(binar)
#     if tank_now - before_azs[binar] >= 0 or tank_now - lent >= 0:
#         # print("be", tank_now)
#         tank_now -= before_azs[binar]
#         lent -= before_azs[binar]
#         if lent <= 0: break
#         if binar == 1:
#             binar = 0
#         else:
#             binar = 1
#         print("benz",tank_now)
#     if tank_now - before_azs[binar] < 0 and not (tank_now - lent >= 0):
#         print("заправился")
#         values += 1
#         tank_now = tank
#         print(before_azs[binar])
#         if before_azs[binar] > tank_now and not (tank_now - lent >= 0):
#             print(-1)
#             exit()
# print(values)

# Office Hours
# list = [int(item) for item in input().split()]
# befor = list[1] + 1
# after = list[0] - list[2]
# print(list[0] - after +1 if after > befor else list[0] - befor + 1)

# Чертов Поликарп
# count = int(input())
# str, st= input(), ''
# set_start, set_end = set(), set()
# for c in str:
#     count -= 1
#     if len(str) == 1 and str.islower():
#         print(1)
#         exit(0)
#     elif c.islower():
#         st += c
#         if count == 0:
#             set_start = set(st)
#             st = ''
#             if len(set_start) >= 2:
#                 set_end |= set_start
#     else:
#         set_start = set(st)
#         st = ''
#         if len(set_start) >= 2:
#             set_end |= set_start
# print(len(set_end))





# Честная игра
# list = []
# for i in range(int(input())):
#     list.append(int(input()))
# set1 = set(list)
# if len(set1) != 2:
#     print("NO")
# elif list.count(set1.pop()) != list.count(set1.pop()):
#     print('NO')
# else:
#     print('YES')
#     Set = set(list)
#     print(Set.pop(),Set.pop())





# Хитрая сумма
# count = int(input())
# for i in range(0, count):
#     number = int(input())
#     sum = ((1 + number)*number)//2
#     # print(sum)
#     sum_square = 0
#     for num in range(0, number + 1):
#         square = 2 ** num
#         if (square) <= number:
#             sum_square += square
#             # print(square)
#         else: break
#     print(sum - (sum_square * 2))


# театральная площадь
# import math
# pl_x, pl_y, plate = input().split()
# a = math.ceil(int(pl_y) / int(plate)) * math.ceil(int(pl_x) / int(plate))
# print(a if a != 0 else 1)





# Отзыв профессора мудди
# def read():
#     sk = []
#     i = int(input())
#     while i != 0:
#         sk.append(input())
#         i -= 1
#     return sk
#
# def analysis(template, Feedback):
#     i = 0
#     for world_f in Feedback:
#         for world_t in template:
#             if world_f == world_t:
#                 i += 1
#     return i
#
# Positive_worlds = (read())
# Negative_worlds = (read())
# Feedback_worlds = (read())
#
# result = analysis(Positive_worlds, Feedback_worlds) - analysis(Negative_worlds, Feedback_worlds)
#
# if result > 0:
#     print('Positive')
# elif result < 0:
#     print('Negative')
# elif result == 0:
#     print('Neutral')










# ЗАДАЧА С СЛОНОМ
# list = []
# list.append(input())
# list.append('')
# i = int(input())
# while i != 0:
#     list.append(input())
#     i -=1
# while len(list) != 0:
#     print(list.pop(0))









# Право лево
# i = int(input())
# groop = 1
# sk = []
# while i != 0:
#     sk.append((input()))
#     i -= 1
#
# old = sk.pop()
# while len(sk) != 0:
#     new = sk.pop()
#     if new != old:
#         groop +=1
#         old = new
#
# print(groop)