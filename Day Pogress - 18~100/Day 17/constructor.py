"""
how to create a class

a class is constructed through constructor

=> a class can be constructed through specific function called    "__init__(self)"
"""


# let's create a Class

class Person:
    """
    A class to create a person with the following attributes:
    age, marks, phone, user_id, profession, goal

    Have the following methods:
    get_age()
    get_marks()
    get_phone()
    get_user_id()
    get_profession()
    get_goal()
    set_age(age)
    set_marks(marks)
    set_phone(phone)
    set_user_id(user_id)
    set_profession(profession)
    set_goal(goal)
    print_details()

    """
    # now we have to define the shape of the class for that we use __init__

    def __init__(self, age, marks, phone, user_id, profession, goal):
        # this is a special function for the initialising the variables
        # construct the shape

        ## to add new parameters we pass in init method

        """
        this is a function to initialise the variables of the class
        :param age: int
        :param marks: int
        :param phone: int
        :param user_id: int
        :param profession: string
        :param goal: string
        """
        self.age = age
        self.marks = marks
        self.phone = phone
        self.user_id = user_id
        self.profession = profession
        self.goal = goal

    def get_age(self):
        """
        this is a function to get the age of the class
        :return: int
        """
        return self.age

    def get_marks(self):
        """
        this is a function to get the marks of the class
        :return: int
        """
        return self.marks

    def get_phone(self):
        """
        this is a function to get the phone of the class
        :return: int
        """
        return self.phone

    def get_user_id(self):
        """
        this is a function to get the user_id of the class
        :return: int
        """
        return self.user_id

    def get_profession(self):
        """
        this is a function to get the profession of the class
        :return: string
        """
        return self.profession

    def get_goal(self):
        """
        this is a function to get the goal of the class
        :return: goal
        """
        return self.goal

    def set_age(self, age):
        """
        this is a function to set the age of the class
        :param age: int
        :return: Age
        """
        self.age = age

    def set_marks(self, marks):
        """
        this is a function to set the marks of the class
        :param marks: int
        :return: marks
        """
        self.marks = marks

    def set_phone(self, phone):
        """
        this is a function to set the phone of the class
        :param phone: int
        :return: phone
        """
        self.phone = phone

    def set_user_id(self, user_id):
        """
        this is a function to set the user_id of the class
        :param user_id: int
        :return: user_id
        """
        self.user_id = user_id

    def set_profession(self, profession):
        """
        this is a function to set the profession of the class
        :param profession: string
        :return: Profession
        """
        self.profession = profession

    def set_goal(self, goal):
        """
        this is a function to set the goal of the class
        :param goal: string
        :return:  goal
        """
        self.goal = goal

    def print_details(self):
        """
        this is a function to print the details of the class
        :return: age , marks , phone , user_id , profession , goal
        """
        print("age: ", self.age)
        print("marks: ", self.marks)
        print("phone: ", self.phone)
        print("user_id: ", self.user_id)
        print("profession: ", self.profession)
        print("goal: ", self.goal)


abhishek = Person(21, 90, 31114111, 12345, "student", "to be a good programmer")
abhishek.set_age(20)
abhishek.set_marks(90)
abhishek.set_phone(9674144556)  # yess this is a valid phone number of mine :)
abhishek.set_user_id(1)
abhishek.set_profession("student")
abhishek.set_goal("to be a good programmer")
print("the address is ")
print(abhishek) # this is the address of the object
print(abhishek.__dict__) # this is a dictionary of the class
print(abhishek.__doc__)  # this is a special function to print the docstring of the class
abhishek.print_details() # this is to print the details of the class

profession = abhishek.get_profession() # this is to get the profession of the class
print("the profession is " + profession) # this is to print the profession of the class