from helpers import Task, ToDoList
from user_registration import Registration
todo_list = ToDoList()
reg = Registration()
enter_1 = True
enter = False
while enter_1 == True:
    print("------------------Меню регистрации и входа:------------------")
    print("1. Регистрация")
    print("2. Вход")
    print("3. Выход")
    choice_reg = input("Выберите действие: ")
    if choice_reg == "1":
        login = input("Enter your login: ")   
        password = input("Enter your password: ")
        reg.append_users(login,password)
        enter = True
        

    elif choice_reg == "2":
        login = input("Enter your login: ")   
        password = input("Enter your password: ")
        reg.check_user(login,password)
        if reg.check_user(login,password) == True:
            enter = True

        

    elif choice_reg == "3":
        break

    else:
            print("Недопустимая команда. Пожалуйста, выберите действие из списка.")
            

    while enter == True:
            print("\nМенеджер списков дел")
            print("1. Добавить задачу")
            print("2. Удалить задачу")
            print("3. Просмотреть задачи")
            print("4. Отметить задачу как выполненную")
            print("5. Упорядочить по приоритету")
            print("6. Упорядочить по сроку выполнения")
            print("7. Выйти")
            print("8. Today taskes")

            choice = input("Выберите действие: ")

            if choice == "1":
                title = input("Введите название задачи: ")
                description = input("Введите описание задачи: ")
                priority = int(input("Введите приоритет (целое число): "))
                due_date = input("Введите срок выполнения (дата): ")
                task = Task(title, description, priority, due_date)
                todo_list.add_task(task)
                print("Задача добавлена.")
                

            elif choice == "2":
                todo_list.view_tasks()
                index = int(input("Введите номер задачи, которую вы хотите удалить: ")) - 1
                if 0 <= index < len(todo_list.tasks):
                    task = todo_list.tasks[index]
                    todo_list.remove_task(task)
                    print("Задача удалена.")
                else:
                    print("Недопустимый номер задачи.")

            elif choice == "3":
                todo_list.view_tasks()

            elif choice == "4":
                todo_list.view_tasks()
                index = int(input("Введите номер задачи, которую вы хотите отметить как выполненную: ")) - 1
                if 0 <= index < len(todo_list.tasks):
                    task = todo_list.tasks[index]
                    todo_list.complete_task(task)
                    print("Задача отмечена как выполненная.")
                else:
                    print("Недопустимый номер задачи.")

            elif choice == "5":
                todo_list.today_tasks()
               
                todo_list.order_by_priority()
                print("Задачи упорядочены по приоритету.")
                pass

            elif choice == "6":
                todo_list.order_by_due_date()
                print("Задачи упорядочены по сроку выполнения.")


            elif choice == "8":
                todo_list.today_tasks()
                           

            elif choice == "7":
                break

            else:
                print("Недопустимая команда. Пожалуйста, выберите действие из списка.")