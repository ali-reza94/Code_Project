# String Type

print("Hello World!")
name = "Ali"
message_1 = "My name is"
print(message_1, name)

city = "Melbourne"
message_2 = f"I live in {city}."
print(message_2)  # Using "f" string. 

# Integer Type
age = 29
message_3 = f"I am {age} years old."  # Using "f" string to combine integer and string type.
print(message_3)

current_year = 2024
message_4 = f"I was born in {current_year - age}."
print(message_4)

# Datetime Type
# Creating a variable for conditional called "debug_mode". 
# This is to create an "if statement" for printing that if you put "True" and not to print when you put "False". 
debug_mode = True
from datetime import datetime  # Importing the datetime library
current_datetime = datetime.now()  # Retrieving extact current "date + time".
current_date = current_datetime.date()  # Extracting only the "date" and not "date + time".
if debug_mode: 
    print(current_date)
date_of_birth = datetime.strptime("1994-09-22 10:00:00", "%Y-%m-%d %H:%M:%S").date()  # Converting string to datetime and extracting only the "date".
if debug_mode:
    print(date_of_birth)
date_delta = current_date - date_of_birth  # Converting datetime to time delta (i.e., time difference).
message_5 = f"Oops! I am actually {date_delta.days} days old." 
print(message_5)
message_6 = f"Which means {round(date_delta.days/365, 2)} many years"  # The "round" function rounds to two decimal points (", 2").
print(message_6)