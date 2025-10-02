# Objects and Classes
# In this exercise you will create a class to model a Training Course object. 

# Use TrainingCourse naming style NOT training_course!

# The class will contain both data and method attributes. 
# The data attributes will consist of a 
# course title,
# a duration ( in days ), 
# a course price and 
# a list of delegate names. 

# The Training Course
# object will also require methods: 
# a method to add a name to the delegate list and 
# a method to display the total revenue generated for the Training Course object.
# hint: the number of delegates will be returned by the built-in len() function

# 1. Create a script called classes_exercise.py.
# 2. Create a class called TrainingCourse
# 3. Add a dunder __init__ method to ensure that a TrainingCourse object is created
# with the following data attributes: title, duration, pricePerPerson and an empty list
# called delegates.
# 4. Add a method called add_delegates that will accept a delegate name as a parameter
# and then append it to the delegates list i.e. self.delegates.append(name).
# 5. Add method called get_total_revenue which will return the total revenue generated for
# the Training Course object i.e. number of delegates * pricePerPerson.

# TEST YOUR Classes
# 6. Create a TrainingCourse object with the data attributes set to the following values:
# title: Python Programming 1
# duration: 4
# price per person: 1600
# delegates: [ ]
# 7. Use the addDelegate method to assign some names to the Training Course
# object’s delegates list.
# 8. Display to the console the total revenue generated for the TrainingCourse object.



class TrainingCourse:
    def __init__(self, title, duration, price_per_person):
        self.title = title
        self.duration = duration
        self.price_per_person = price_per_person
        self.delegates = []
    def add_delegate(self, name):
        self.delegates.append(name)
    def get_total_revenue(self):
        return self.price_per_person *len(self.delegates)
    def __str__(self):
            return f"""
Course Title: {self.title}
Duration (days): {self.duration}
Price Per Person: {self.price_per_person}
Delegates booked: {self.delegates}"""

python_1 = TrainingCourse("Python Programming 1", 4, 1600.00)
python_1.add_delegate("Suki")
python_1.add_delegate("Graham")

print(total_revenue := f"£{python_1.get_total_revenue()}")
print(python_1.__str__())
print(python_1)
