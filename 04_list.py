# create a list

sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"] # list()

# Indexing, Slicing
sample_ele = sample_list[1]
print(sample_ele)

# sample_ele = sample_list[5]
# print(sample_ele)

"""
Traceback (most recent call last):
  File "C:\devops\daws-78s\repos\python-devops\04_list.py", line 9, in <module>
    sample_ele = sample_list[5]
                 ~~~~~~~~~~~^^^
IndexError: list index out of range
"""

sample_ele = sample_list[-1] # sample_list[-1]
print(sample_ele)

sample_ele = sample_list[len(sample_list) - 1] # sample_list[len(sample_list) - 1]
print(sample_ele)

# Slicing
sliced_list = sample_list[1:3] # ["Terraform", "Jenkins"]
print(sliced_list)

sliced_list_len = len(sliced_list)
print(sliced_list_len)

# List is amutable data type
# Once defined, it can be altered
sample_list[1] = "Shell"
print(sample_list)

# Append element to the list
sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]
sample_list.append("Shell") # Inplace operation
print(sample_list)

# Append list to list
sample_list.append(sample_list)
print(sample_list)

sample_list.append(sample_list)
print(len(sample_list))
print(sample_list[-1])

last_element = sample_list[-1]
print(last_element)

last_element = sample_list[len(sample_list) - 1]
print(last_element)

# Extend
sample_list = [1, 2, 'sample', True]
sample_list.extend(sample_list)
print(len(sample_list), sample_list)

# Membership operator
is_elem = 2 in sample_list
print(is_elem)

""" 
>>> sample_list = [1, 2, 'sample', True]
>>> sample_list.extend(sample_list)
>>> print(len(sample_list), sample_list)
8 [1, 2, 'sample', True, 1, 2, 'sample', True]
>>> sample_list = [1, 2, 'sample', True]
>>> sample_list.append([4,5])
>>> print(sample_list)
[1, 2, 'sample', True, [4, 5]]
>>> sample_list.extend([4, 5])
>>> print(sample_list)
[1, 2, 'sample', True, [4, 5], 4, 5]
>>> sample_list[-3][-1]
5
>>> sample_list[-4][-2] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bool' object is not subscriptable
>>> sample_list[-3][-2] 
4
>>> sample_list[-3][-1] 
5
>>> sample_list[-3][0] 
4 
>>> [1, 2, 'sample', True] + [4, 5]
[1, 2, 'sample', True, 4, 5]
>>> sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]
>>> sample_list.clear()
>>> sample_list.append("Shell")
>>> sample_list
['Shell']
>>>
"""