import random as ran
from modulsofgames import stack
from modulsofgames import persons
from modulsofgames import marker

#  3 кучи камней

for i in range(3):
    stack.append(ran.randint(1, 10))
#  Взять из кучи камень


def choose_and_take(par1, par2):
    if 0 < par1 <= 3 and par2 <= stack[par1-1]:
        stack[par1 - 1] = stack[par1 - 1] - par2
    else:
        new_stack = int(input('Игрок сделай снова выбор кучи: '))
        new_count = int(input('Игрок сделай снова выбор камней: '))
        choose_and_take(par1=new_stack, par2=new_count)

    # print(stack)


#  Проверить кучу на наличие камней


def check_stack(par1):
    if any(par1):
        print('продолжим')
        print(par1)
    else:
        if marker.flag % 2 == 1:
            print(f'Все камни закончились победил {persons.person_1}')
        else:
            print(f'{stack}Все камни закончились победил {persons.person_2}')
        print('Game Over')



#  Передавать ход другому игроку

def step_by_step(par):
    print('Начало игры "Повелитель камней"\nВ ней побеждает тот кто заберет последний камень! ')
    print(f'Создалась куча камней\n{par}')
    while any(par):

        if marker.flag % 2 == 0:
            player2_stack = int(input(f'{persons.person_2} выбери кучу: '))
            count_2_p = int(input(f'{persons.person_2} выбери количество камней: '))

            choose_and_take(player2_stack, count_2_p)

            check_stack(par)

        elif marker.flag % 2 == 1:
            player1_stack = int(input(f'{persons.person_1} выбери кучу: '))
            count_1_p = int(input(f'{persons.person_1} выбери количество камней: '))

            choose_and_take(player1_stack, count_1_p)

            check_stack(par)
        marker.flag += 1


step_by_step(stack)
