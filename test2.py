name = input("Input task name: ")
with open('taskes.txt', 'r') as file:
    lines = file.readlines()
with open('taskes.txt', 'r') as file:
    for line in lines:
        if line.split()[0] == name:
            str_line = str(line)
            print(str_line)
            print(str_line.split("|"))
            split_line = str_line.split("|")
            print(split_line[2].split())
            print(split_line[2].split()[1])
            split_line_2_split_1 =  split_line[2].split()[1]

            split_line_2_split_1 = "lol "
            print(split_line_2_split_1)

            


            # print(line.split("|")[2])
            # line_split_2 = line.split("|")[2]

            # print(line_split_2.split()[1])
            # line_split_2_1 = line_split_2.split()[1]
                    
            # print(line)



# txt = 'one one was a race horse, two two was one too.'

# x = txt.replace('one', 'three')

# print(x)
