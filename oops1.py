# initiate the class
class employee:
    # special func/method -constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "abc" 
        print("Attributes/data have been initiated")

    def travel(self,destination):
        print("Travelled function called manually")
        print(f"Employee is now travelling to {destination}")
        

# create an obj/instance of the class
sam = employee()
# printing the attributes
# print(sam.id)

# calling a method
sam.travel("Vadodara")