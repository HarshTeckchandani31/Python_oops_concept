class chatbook:
    def __init__(self):
        self.name = "Default user"
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input =input("""welcome to chatbook !! how you would like to proceed?
        1. press 1 for signup
        2. press 2 for signin
        3. press 3 to write a post
        4. press 4 to message a friend
        5. press any key to exit \n""")

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.msg_friend()
        else:
            exit()
    
    
    def signup(self):
        email = input("Enter Email ID->  ")
        pwd = input("Enter Password here->  ")
        self.username = email
        self.password = pwd
        print("Signup successful !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username =='' and self.password =='':
            print("Please signup first by pressing 1 in the menu !!")
        else:
            uname = input("Enter your email/username here ---> ")
            pwd = input("Enter your password here ---->")
            if self.username == uname and self.password ==pwd :
                print("signin successful !!!")
                self.loggedin = True
            else:
                print("invalid username or password !!")
        print("\n")
        self.menu()
    
    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter you message here--->  ")
            print(f"your post has been created as given below \n {txt}")
        else:
            print("you are not logged in !!")   
        print("\n")
        self.menu()
    
    def msg_friend(self):
        if self.loggedin == True:
            # friend = input("Enter your friend's email here --->")
            msg = input("Enter your message here --->")
            frnd = input("Whom to send the message? --->  ")
            print(f"message has been sent to {frnd} as given below \n {msg}")
        else:
            print("you are not logged in !!")
        print("\n")
        self.menu()
# obj = chatbook()