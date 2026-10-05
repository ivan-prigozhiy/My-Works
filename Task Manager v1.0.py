import sys
import os


all_tasks = ['Clean up', 'Wash the dishes', 'Do Homework', 'Feed the cat', 'Take out the trash']



def clear():
    os.system("cls")



def t_enter():
    input('\n> Type Enter... ')



def show_all(numbered=False):
    clear()
    if len(all_tasks) == 0:
        print('\nNot added any tasks yet')
        t_enter()
        return

    print("\n===== TASK MANAGER =====", end='\n\n')
    for s in all_tasks:
        print(f" {(all_tasks.index(s) + 1) if numbered else '•'}{'.' if numbered else ''} {s}")



def add_task():
    n = input('\n> Type name of task: ').strip()
    if n == '':
        print('\nYou can\'t add nothing!')
        t_enter()
    elif n.isdigit():
        print('\nTask name can\'t consist only of numbers!')
        t_enter()
    elif n in all_tasks:
        print('\nThis task is already added')
        t_enter()
    else:
        all_tasks.append(n)
        print(f'\nSuccessfully added new task ({n})')
        t_enter()



def del_task():
    if len(all_tasks) == 0:
        print('\nNot added any tasks yet')
        t_enter()
        return
    show_all(True)
    i = input("\n> Type what do you want to delete: ").strip()
    if i.isdigit():
        if 1 <= int(i) <= len(all_tasks):
            n = input(f'\nAre you sure you want to delete this task ({all_tasks[int(i) - 1]})? (y/n)\n\n> ').strip().lower()
            if n == 'y':
                print('\nTask was successfully deleted ✓')
                all_tasks.pop(int(i) - 1)
                t_enter()
            elif n == 'n':
                print('\nTask wasn\'t deleted')
                t_enter()
            else:
                print('\nYou were supposed to enter "y" or "n"!')
                t_enter()
        else:
            print('\nNumber is invalid!')
            t_enter()

    else:
        if i in all_tasks:
            n = input(f'\nAre you sure you want to delete this task (\'{i}\')? (y/n)\n\n> ').strip().lower()
            if n == 'y':
                print('\nTask was successfully deleted ✓')
                all_tasks.remove(i)
                t_enter()
            elif n == 'n':
                print('\nTask wasn\'t deleted ✗')
                t_enter()
            else:
                print('\nYou were supposed to enter "y" or "n"!')
                t_enter()
        else:
            print('\nTask wasn\'t found')
            t_enter()



while True:
    clear()

    print("\n===== TASK MANAGER =====", end='\n\n')
    print(" 1. Show tasks")
    print(" 2. Add task")
    print(' 3. Delete task')
    print(" 0. Exit")

    choice = input("\n> ").lower().strip()
    if choice == "1":
        show_all()
        t_enter()

    elif choice == "2":
        add_task()

    elif choice == "3":
        del_task()

    elif choice == "0":
        n = input('\nAre you sure you want to exit? (y/n)\n\n> ').strip().lower()
        if n == 'y':
            print('\nSee you next time! -_-')
            t_enter()
            sys.exit()
        elif n == 'n':
            continue
        else:
            print('\nYou were supposed to enter "y" or "n"!')
            t_enter()
    else:
        print('\nYou were supposed to enter number (0-3)!')
        t_enter()