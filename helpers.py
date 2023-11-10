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

    def add_task(self, task):
        self.tasks.append(task)
        with open("taskes.txt","r") as file:
                file.read().splitlines()
        with open("taskes.txt","a") as file:
                    file.write(f"{task.title} - priority: {task.priority} : | due_date: {task.due_date} |status:Not completed\n")

        


  

         

    def remove_task(self):
            name = input("Input task name: ")
            with open('taskes.txt', 'r') as file:
                lines = file.readlines()
            with open('taskes.txt', 'w') as file:
                for line in lines:
                    if not line.startswith(name):
                        file.write(line)
                print("task was deleted")

    def view_tasks(self):
          with open("taskes.txt","r") as file:
                
                for line in file.read().splitlines():
                    print(line)

    def today_taskes_2(self):            
        with open("taskes.txt","r") as file:
                    for line in file.read().splitlines():
                        line_split = line.split("|")

                        line_split_1 = str(line_split[1])
                        
                        line_split_1_1 = line_split_1.split(":")
                        line_split_1_1_1 = line_split_1_1[1]
                        line_splited_to_str_nums = line_split_1_1_1.split("-")
                        line_splited_to_str_nums_day = int(line_splited_to_str_nums[0])
                        line_splited_to_str_nums_month = int(line_splited_to_str_nums[1])
                        line_splited_to_str_nums_year = int(line_splited_to_str_nums[2])
                        if line_splited_to_str_nums_day == day_now and line_splited_to_str_nums_month == month_now and line_splited_to_str_nums_year == year_now:
                                print(line) 
                            
                                    

    def complete_task(self):
        name = input("Input task name: ")
        with open('taskes.txt', 'r') as file:
            lines = file.readlines()
        with open('taskes.txt', 'w') as file:
            for line in lines: 
                line_split = line.split('|')
                print(line_split)
               
                if name ==line_split[0].split("-")[0].strip():
                    print(line_split[0].split("-")[0].strip())
    
                    if line_split[2].strip() == 'status:Not completed':
                        line_split[2] = 'status: Completed\n'
                    line = '|'.join(line_split)
                file.write(line)
                       
                               
        

    def order_by_priority(self):
        sort_list = []
        sort_prior = []
        # self.tasks.sort(key=lambda task: task.priority)
        with open('taskes.txt', 'r') as file:
            lines = file.readlines()
            with open('taskes.txt', 'r') as file:
                for line in lines:
                        sort_list.append(line)
                        sort_prior.append(line.split(":")[1])


            
            print(sort_prior)
            sorted_prior = sorted(sort_prior)
            print(sorted_prior)
                        
            print(sort_list) 
            print(str(sort_list[0]).split("|")[0].split(":")[1])
            # for i in range(1,len(sort_list)):
            #     print(i)
            for i in range(len(sort_list)):
                
                # print(str(sort_list[i]).split("|")[0].split(":")[1])
                if sorted_prior[i] == str(sort_list[i]).split("|")[0].split(":")[1]:
                    print(sort_list[i])
                    # print(str(sort_list[i]).split("|")[0].split(":")[1])
              
           
            
                  
                      
                 
                 
                  


    def order_by_due_date(self):
        self.tasks.sort(key=lambda task: task.due_date)
