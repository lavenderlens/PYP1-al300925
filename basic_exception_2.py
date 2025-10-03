class TrainingCourse:
    # as it stands, a TrainingCourse object may be created with null or empty fileds
    # supposing we wanted to code against this:
    def __init__(self, title, duration, price_per_person):
        self.set_title(title)#Exception: you must enter a title
        self.duration = duration
        self.price_per_person = price_per_person
        self.delegates = []
    def set_title(self, title):
        if title != "":
            self.title = title
        else:
            # print("you must enter a title")#doesn't stop object creation
            # to stop the code in its tracks we need to generate our own exception
            raise Exception("you must enter a title")#Exception: you must enter a title
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

try:
    python_2 = TrainingCourse("", 4, 1600.00)#code will stop here, generate stack trace Exception: you must enter a title
except Exception:
     print("TrainingCourse object could not be created at this time")
    #  exception has stopped the object existing

my_courses = []
try:
    my_courses.append(python_1)
    my_courses.append(python_2)
except NameError:
     print("One or more courses do not exist")
for course in my_courses:
     print(course)#AttributeError: 'TrainingCourse' object has no attribute 'title'
