#----------------------------------------   Context Managers in OOP   ---------------------------------------------------------#
#                                        -----------------------

"""
In Python, context managers are used to properly manage resources by ensuring that they are acquired and released
at appropriate times. They are commonly used with the `with` statement, which provides a concise syntax for resource management.

In Object-Oriented Programming (OOP), custom context managers can be implemented by defining special methods
within a class: `__enter__` and `__exit__`.

Context managers are useful for managing resources like database connections, threads, locks, and more, beyond just file handling.
"""
#----------------------------------------------------------------------------------------------------------------------#

# Key Points about Context Managers in OOP:
'''
- Context Manager: A design pattern for managing resources.
- __enter__ Method: Defines the initialization or setup process when entering the context.
- __exit__ Method: Defines the cleanup process when exiting the context.
- The `with` Statement: Used to invoke context managers, ensuring proper setup and cleanup.
- Benefits: Improves code readability, ensures resource cleanup, and reduces boilerplate code.
- Use Cases: Managing database connections, locks, sockets, threads, etc.
'''
#----------------------------------------------------------------------------------------------------------------------#

# Defining a Custom Context Manager

class ManagedResource:
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.resource = None

    def __enter__(self):
        # Setup or acquire resource
        self.resource = f"Resource {self.resource_name} acquired"
        print(self.resource)
        return self.resource  # This value is assigned to the variable after 'as' in the 'with' statement

    def __exit__(self, exc_type, exc_value, traceback):
        # Cleanup or release resource
        print(f"Releasing {self.resource_name}")
        self.resource = None

# Using the Custom Context Manager

with ManagedResource("MyResource") as resource:
    print(f"Using {resource}")

# Output:
# Resource MyResource acquired
# Using Resource MyResource acquired
# Releasing MyResource

#----------------------------------------------------------------------------------------------------------------------#

# Advanced Context Manager Example: Managing a Database Connection

class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    def __enter__(self):
        # Simulate establishing a database connection
        self.connection = f"Connection to {self.connection_string} established"
        print(self.connection)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        # Simulate closing the database connection
        print(f"Closing connection to {self.connection_string}")
        self.connection = None

# Using the DatabaseConnection Context Manager

with DatabaseConnection("example_db") as db_conn:
    print(f"Performing operations on {db_conn}")

# Output:
# Connection to example_db established
# Performing operations on Connection to example_db established
# Closing connection to example_db

#----------------------------------------------------------------------------------------------------------------------#
