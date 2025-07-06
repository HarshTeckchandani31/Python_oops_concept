# initiate the class
class employee:
    # special func/method -constructor
    def __init__(self):
        # print("Started executing attributes/data")
        # print(id(self))
        self.id = 123
        self.salary = 50000
        self.designation = "abc" 
        # print("Attributes/data have been initiated")

    def travel(self):
        print("Travelled function called manually")
        print(f"Employee is now travelling to Vadodara")
        

# create an obj/instance of the class
sam = employee()
# sam.name = "samsheer"
# print(sam.name)
# print(id(sam))
# printing the attributes
# print(sam.id)

# calling a method
# sam.travel() 
# print(type(sam))