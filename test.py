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
                # spl6 = str(line_split[6])
                # print(str(line_split[6]))
                # print(str(line_split[6]).split('-'))
                # line_split_6 = str(line_split[6]).split('-')
                # day_user_input = int(line_split_6[0])
                # month_user_input = int(line_split_6[1])
                # year_user_input = int(line_split_6[2])
                # print(day_user_input)
                # print(month_user_input)
                # print(year_user_input)
                # if day_user_input == day_now and month_user_input == month_now and year_user_input == year_now:
                #         print(line)
                
                

                # if spl6 == day_now:
                #         print(line)
                
                    
