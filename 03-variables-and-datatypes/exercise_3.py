# Built-in data types
# In this exercise you will create a script comprising airline passenger information. You
# must choose the most appropriate data type for each item of data. In practice, it is
# unlikely that you will hard-code data into a script in this manner, but the purpose of the
# exercise is to make you familiar with the built-in data types at your disposal. Don't forget
# about Python's naming conventions.
# 1. Create a script named ch3_data_types.py.
# 2. Declare and assign one variable for each of the items of data tabled below.

# Description             Value
# ID                      1234
# First name              John
# Last name               Doe
# Checked bags            False
# Visited countries       Latvia, Guyana, Yemen, Uzbekistan
# Flight                  LGW to CDG
# Flight time             1 hour 15 minutes

# 3. Print each variable and its data type to the console.

id = 1234
first_name = "John"
last_name = "Doe"
checked_bags = False
visited_countries = ["Latvia", "Guyana", "Yemen", "Uzbekistan"]
visited_countries.append("USA")
flight = {"DEP":"LGW", "ARR": "CDG"}
flight_rtn = {"DEP":"CDG", "ARR": "LGW"}
flight_time_in_mins = 75
flight_time_in_hours = 1.25
flight_time_in_hours_and_mins = {"hours": 1, "mins": 15}

