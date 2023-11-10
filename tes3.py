# # name = input("Input task name: ")
# with open('taskes.txt', 'r') as f1:
#     lines = f1.readlines()

#     for line in lines:
#         # if line.split()[0] == name:

#             print(line)
#             line.split()[0] = ' '
#             print(line.split()[0])

# with open('taskes.txt','r') as file:
#       lines = file.read().splitlines()
#       for line in lines:
#             print(line)
            
            # file.write(line.split()[0])         
            # lines.insert(2, 'new line\n')
        # line = line.strip()
        # if line == 'искомая строка':
        #     f2.write('новая строка\n')
        # else:
        #     f2.write(line)

def mark_task_as_completed(self):
        name = input("Input task name: ")
        with open('task.txt', 'r') as file:
            lines = file.readlines()
        with open('task.txt', 'w') as file:
            for line in lines:
                line_split = line.split('|')
                if name == line_split[0].strip():
                    if line_split[4].strip() == 'Not completed':
                        line_split[4] = 'Completed\n'
                    line = '|'.join(line_split)
                file.write(line)