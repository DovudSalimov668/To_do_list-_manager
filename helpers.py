import datetime
from datetime import datetime
date_string = datetime.today()
format_string_day = "%d"
format_string_month = "%m"
format_string_year = "20%y"
day_now = int(datetime.strftime(date_string,format_string_day))
month_now = int(datetime.strftime(date_string,format_string_month))
year_now = int(datetime.strftime(date_string,format_string_year))
              

class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.is_completed = False

    

class ToDoList:
    def __init__(self):
        self.tasks = []

    # def __str__(self):
    #     return self.tasks    

    def add_task(self, task):
        self.tasks.append(task)


    def append_taskes(self,title: str, description: str, priority: str, due_date:int):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date        
        with open("taskes.txt","r") as file:
            file.read().splitlines()
        with open("taskes.txt","a") as file:
            file.write(f"{title}:{description}:{priority}:{due_date}\n") 
            print("успешно сохранены.")   
        with open("taskes.txt","r") as file:
             for line in file.read().splitlines():
                line_split = line.split(':')
              
                if line_split[3] == day_now:
                    print(line)
                    return True


         

    def remove_task(self, task):
        self.tasks.remove(task)

    def view_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        for index, task in enumerate(self.tasks,1):
            if task.is_completed:
                status = "Completed"
            else:
                status = ("Not completed" )  

            print(f"{index}. {task.title} - Приоритет: {task.priority}, Срок: {task.due_date}, Статус: {status}")
            with open("taskes.txt","r") as file:
                file.read().splitlines()
            with open("taskes.txt","a") as file:
                file.write(f"{index}. {task.title} - priority: {task.priority} | due_date: {task.due_date} | status: {status}\n")

        
    def today_tasks(self):
                            
        with open("taskes.txt","r") as file:
            for line in file.read().splitlines():
                line_split = line.split()
                line_split_6 = str(line_split[6]).split('-')
                day_user_input = int(line_split_6[0])
                month_user_input = int(line_split_6[1])
                year_user_input = int(line_split_6[2])
                if day_user_input == day_now and month_user_input == month_now and year_user_input == year_now:
                        print(line)


    def today_taskes_2(self):
                      
        with open("taskes.txt","r") as file:
                    for line in file.read().splitlines():
                        line_split = line.split("|")
                        # print(line_split)
                        # print(str(line_split[1].split(":")).split("-"))
                        line_split_1 = str(line_split[1])
                        # print(line_split_1.split(":"))
                        line_split_1_1 = line_split_1.split(":")
                        line_split_1_1_1 = line_split_1_1[1]
                        line_splited_to_str_nums = line_split_1_1_1.split("-")
                        line_splited_to_str_nums_day = int(line_splited_to_str_nums[0])
                        line_splited_to_str_nums_month = int(line_splited_to_str_nums[1])
                        line_splited_to_str_nums_year = int(line_splited_to_str_nums[2])
                        # print(int(line_splited_to_str_nums_day))
                        # print(int(line_splited_to_str_nums_month))
                        # print(int(line_splited_to_str_nums_year))

                        if line_splited_to_str_nums_day == day_now and line_splited_to_str_nums_month == month_now and line_splited_to_str_nums_year == year_now:
                                print(line)                    
                                    

    def complete_task(self, task):
        task.is_completed = True

    def order_by_priority(self):
        self.tasks.sort(key=lambda task: task.priority)

    def order_by_due_date(self):
        self.tasks.sort(key=lambda task: task.due_date)
