#----------------------------------------   Nested Dictionaries   ------------------------------------------------#
#                                            ---------------------

"""
A nested dictionary is a dictionary inside another dictionary. It allows for the creation of more complex data structures.
Nested dictionaries can be used for representing hierarchical data like trees or nested configurations.
"""

# Key Points about Nested Dictionaries:
'''
1. A nested dictionary is simply a dictionary as a value for a key in another dictionary.
2. Accessing nested dictionaries requires multiple levels of key access.
3. Nested dictionaries are commonly used for more complex data representation (e.g., JSON-like structures).
'''

#----------------------------------------------------------------------------------------------------------------------#

# Example of a Nested Dictionary
my_dict = {
    "person": {
        "name": "Alice",
        "age": 30,
        "location": "Wonderland"
    },
    "job": {
        "title": "Engineer",
        "department": "Research"
    }
}
print("Nested Dictionary:", my_dict)

# 1. Accessing Nested Dictionary Elements
"""
To access nested dictionary elements, use multiple keys.
"""
person_name = my_dict["person"]["name"]
job_title = my_dict["job"]["title"]
print("Person's name:", person_name)
print("Job title:", job_title)

# 2. Modifying Nested Dictionary Elements
"""
You can modify nested dictionary elements just like any other dictionary.
"""
my_dict["person"]["age"] = 31
my_dict["job"]["department"] = "Development"
print("Modified Nested Dictionary:", my_dict)

# 3. Adding New Nested Elements
"""
New keys can be added inside the nested dictionary structure.
"""
my_dict["person"]["hobby"] = "Reading"
print("After Adding Hobby:", my_dict)

#----------------------------------------------------------------------------------------------------------------------#
