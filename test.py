import datetime
from datetime import datetime
date_string = datetime.today()
format_string_day = "%d"
format_string_month = "%m"
format_string_year = "20%y"
day_now = int(datetime.strftime(date_string,format_string_day))
month_now = int(datetime.strftime(date_string,format_string_month))
year_now = int(datetime.strftime(date_string,format_string_year))
              
with open("taskes.txt","r") as file:
            for line in file.read().splitlines():
                line_split = line.split("|")
                print(line_split)
                print(str(line_split[1].split(":")).split("-"))
                line_split_1 = str(line_split[1])
                print(line_split_1.split(":"))
                line_split_1_1 = line_split_1.split(":")
                line_split_1_1_1 = line_split_1_1[1]
                line_splited_to_str_nums = line_split_1_1_1.split("-")
                line_splited_to_str_nums_day = int(line_splited_to_str_nums[0])
                line_splited_to_str_nums_month = int(line_splited_to_str_nums[1])
                line_splited_to_str_nums_year = int(line_splited_to_str_nums[2])
                print(int(line_splited_to_str_nums_day))
                print(int(line_splited_to_str_nums_month))
                print(int(line_splited_to_str_nums_year))

                if line_splited_to_str_nums_day == day_now and line_splited_to_str_nums_month == month_now and line_splited_to_str_nums_year == year_now:
                        print(line)
                        


              