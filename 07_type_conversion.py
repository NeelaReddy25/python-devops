sample_str = "This is a sample string"
sample_str_list = list(sample_str)
print(sample_str_list)

sample_str_tuple = tuple(sample_str)
print(sample_str_tuple)

# Accept input from a user
user_input = input("Enter a number:")
print(user_input, type(user_input))

# add_10 = user_input + 10
# print(add_10)

"""
Traceback (most recent call last):
  File "C:\devops\daws-78s\repos\python-devops\07_type_conversion.py", line 12, in <module>
    add_10 = user_input + 10
             ~~~~~~~~~~~^~~~
TypeError: can only concatenate str (not "int") to str
"""

add_10 = int(user_input) + 10
print(add_10)