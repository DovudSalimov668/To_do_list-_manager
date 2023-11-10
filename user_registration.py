

class Registration:

    def append_users(self,login:str,password: str):
        with open("users.txt","r") as file:
            file.read().splitlines()
        with open("users.txt","a") as file:
            file.write(f"{login}:Login_password:{password}\n") 
            print("Ваш логин и пароль успешно сохранены.")  

    def check_user(self,login:str,password: str):
        
        self.login =  login
        self.password = password
        with open("users.txt","r") as file:
            for line in file.read().splitlines():
                line_split = line.split(':Login_password:')
              
                if line_split[0] == login and line_split[1] == password:
                    print("We have that user.")
                    check = True

                    return check
                else:  
                    # check = False
                    # print("We don't have that one.")   
                    pass
        
                
