sample_dict = {1: 1, 2: 4, 3: 9} # dict()
# keys in dictionary should of immutable datatype
print(sample_dict[3])

sample_dict = {1: 1, 2: 4, 3: 9, 3: 15}
print(sample_dict[3])

sample_dict = {(1, 2, 3, 4): 1, 2: 4, 3: 9}
print(sample_dict[(1, 2, 3, 4)])

sample_dict = {"1": 1, 2: 4, 3: 9}
print(sample_dict["1"])

# sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
# print(sample_dict[[1, 2, 3, 4]])

"""
Traceback (most recent call last):
  File "C:\devops\daws-78s\repos\python-devops\05_dict.py", line 12, in <module>
    print(sample_dict[[1, 2, 3, 4]])
          ~~~~~~~~~~~^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
"""
dict_keys = sample_dict.keys()
dict_values = sample_dict.values()
dict_items = sample_dict.items()
print(dict_keys, dict_values, dict_items)

# what happens if you access a key that is not present inside a dict
sample_dict = {"1": 1, 2: 4, 3: 9}
print(sample_dict.get(1)) # None
print(sample_dict[1]) # Error

"""
Traceback (most recent call last):
  File "C:\devops\daws-78s\repos\python-devops\05_dict.py", line 32, in <module>
    print(sample_dict[1]) # Error
          ~~~~~~~~~~~^^^
KeyError: 1
"""