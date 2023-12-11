import random as ran
from modulsofgames import stack
from modulsofgames import persons
from modulsofgames import marker
from termcolor import cprint, colored
#  3 кучи камней

for i in range(3):
    stack.append(ran.randint(1, 10))
#  Взять из кучи камень


def choose_and_take(par1, par2):
    if 0 < par1 <= 3 and par2 <= stack[par1-1]:
        stack[par1 - 1] = stack[par1 - 1] - par2
    else:
        new_stack = int(input(colored('Игрок сделай снова выбор кучи: ',color='red')))
        new_count = int(input(colored('Игрок сделай снова выбор камней: ', color='red')))
        choose_and_take(par1=new_stack, par2=new_count)

    # print(stack)


#  Проверить кучу на наличие камней


def check_stack(par1):
    if any(par1):
        cprint('продолжим', color='green')
        cprint(par1, color='green')
    else:
        if marker.flag % 2 == 1:
            cprint(f'Все камни закончились победил {persons.person_1}', color='yellow')
        else:
            cprint(f'{stack}Все камни закончились победил {persons.person_2}', color='yellow')
        print(colored('Game Over', color='green', on_color='on_red', attrs=['underline']))




#  Передавать ход другому игроку

def step_by_step(par):
    cprint('Начало игры "Повелитель камней"\nВ ней побеждает тот кто заберет последний камень! ', color='blue')
    cprint(f'Создалась куча камней\n{par}', color='green')
    while any(par):

        if marker.flag % 2 == 0:
            player2_stack = int(input(colored(f'{persons.person_2} выбери кучу: ', color='magenta')))
            count_2_p = int(input(colored(f'{persons.person_2} выбери количество камней: ', color='magenta')))

            choose_and_take(player2_stack, count_2_p)

            check_stack(par)

        elif marker.flag % 2 == 1:
            player1_stack = int(input(colored(f'{persons.person_1} выбери кучу: ', color= 'yellow')))
            count_1_p = int(input(colored(f'{persons.person_1} выбери количество камней: ', color= 'yellow')))

            choose_and_take(player1_stack, count_1_p)

            check_stack(par)
        marker.flag += 1


step_by_step(stack)
