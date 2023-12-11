# import random as ran
# import stack
#
# #  3 кучи камней
#
# for i in range(3):
#     stack.stack.append(ran.randint(1, 10))
# print(stack.stack)
#
#
# #  Взять из кучи камень
#
# # x = stack[0] = 1
# # print(stack)
#
# def choose_and_take(par1, par2):
#     if 0 < par1 <= 3:
#         ss = stack.stack
#         ss[par1 - 1] = ss[par1 - 1] - par2
#     else:
#         print('касяк')
#     print(stack.stack)
#
#
# def check_stack(par1):
#     if not all(par1):
#         print('продолжим')
#     else:
#         print('END')
#
# xxx = True
#
# while xxx>0:
#     player1_stack = int(input('Выбери кучу'))
#     count_1_p = int(input('Выбери количество камней'))
#
#     choose_and_take(player1_stack, count_1_p)
#
#     check_stack(stack.stack)
#
#     player2_stack = int(input('Выбери кучу'))
#     count_2_p = int(input('Выбери количество камней'))
#
#     choose_and_take(player2_stack, count_2_p)
#
#     check_stack(stack.stack)