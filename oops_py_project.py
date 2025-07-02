class chatbook:
    def __init__(self):
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
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
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
obj = chatbook()