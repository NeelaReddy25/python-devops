sample_set = {1, 2, 5, 4, 2, 3}
print(sample_set)

# Set returns unique elememts that is stored insode that variable
# Sets don't consider the order of insertion
# Set is also a mutable datatype
# Sets don't support indexing

sample_set = {1, 2, 5, 4, 2, 3}
sample_set.add(6)
print(sample_set)
#print(sample_set[2])

"""
Traceback (most recent call last):
  File "C:\devops\daws-78s\repos\python-devops\06_sets.py", line 12, in <module>
    print(sample_set[2])
          ~~~~~~~~~~^^^
TypeError: 'set' object is not subscriptable
"""

# Intersection(), union()