#---------------------------------------- Python Operators Overview ---------------------------------------------------#
#                                        ---------------------------

"""
Operators are special symbols in Python that perform specific operations on variables and values.
Python supports the following types of operators:
1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Assignment Operators
5. Bitwise Operators
6. Identity Operators
7. Membership Operators
"""

#----------------------------------------------------------------------------------------------------------------------#

# 1. Arithmetic Operators
'''
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

Operator         Description                 Example
--------         -----------                 -------
+                Addition                    a + b
-                Subtraction                 a - b
*                Multiplication              a * b
/                Division                    a / b
%                Modulus (remainder)         a % b
**               Exponentiation              a ** b
//               Floor division              a // b
'''

# Examples of Arithmetic Operators
print("Arithmetic Operators:")
a, b = 10, 3
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Modulus (a % b):", a % b)
print("Exponentiation (a ** b):", a ** b)
print("Floor Division (a // b):", a // b)

#----------------------------------------------------------------------------------------------------------------------#

# 2. Comparison Operators
'''
Comparison operators are used to compare values. They return `True` or `False`.

Operator         Description                      Example
--------         -----------                      -------
==               Equal to                         a == b
!=               Not equal to                     a != b
>                Greater than                     a > b
<                Less than                        a < b
>=               Greater than or equal to         a >= b
<=               Less than or equal to            a <= b
'''

# Examples of Comparison Operators
print("\nComparison Operators:")
print("Equal to (a == b):", a == b)
print("Not equal to (a != b):", a != b)
print("Greater than (a > b):", a > b)
print("Less than (a < b):", a < b)
print("Greater than or equal to (a >= b):", a >= b)
print("Less than or equal to (a <= b):", a <= b)

#----------------------------------------------------------------------------------------------------------------------#

# 3. Logical Operators
'''
Logical operators are used to combine conditional statements.

Operator         Description               Example
--------         -----------               -------
and              Logical AND               a and b
or               Logical OR                a or b
not              Logical NOT               not a
'''

# Examples of Logical Operators
print("\nLogical Operators:")
x, y = True, False
print("Logical AND (x and y):", x and y)
print("Logical OR (x or y):", x or y)
print("Logical NOT (not x):", not x)

#----------------------------------------------------------------------------------------------------------------------#

# 4. Assignment Operators
'''
Assignment operators are used to assign values to variables.

Operator         Description               Example
--------         -----------               -------
=                Assign                    a = b
+=               Add and assign            a += b
-=               Subtract and assign       a -= b
*=               Multiply and assign       a *= b
/=               Divide and assign         a /= b
%=               Modulus and assign        a %= b
**=              Exponentiate and assign   a **= b
//=              Floor divide and assign   a //= b
'''

# Examples of Assignment Operators
print("\nAssignment Operators:")
c = 5
print("Initial value (c):", c)
c += 2
print("After c += 2:", c)
c *= 3
print("After c *= 3:", c)
c //= 2
print("After c //= 2:", c)

#----------------------------------------------------------------------------------------------------------------------#

# 5. Bitwise Operators
'''
Bitwise operators perform bit-level operations.

Operator         Description                 Example
--------         -----------                 -------
&                AND                         a & b
|                OR                          a | b
^                XOR                         a ^ b
~                NOT                         ~a
<<               Left shift                 a << 2
>>               Right shift                a >> 2
'''

# Examples of Bitwise Operators
print("\nBitwise Operators:")
d, e = 6, 3  # Binary: d = 110, e = 011
print("Bitwise AND (d & e):", d & e)
print("Bitwise OR (d | e):", d | e)
print("Bitwise XOR (d ^ e):", d ^ e)
print("Bitwise NOT (~d):", ~d)
print("Left Shift (d << 2):", d << 2)
print("Right Shift (d >> 2):", d >> 2)

#----------------------------------------------------------------------------------------------------------------------#

# 6. Identity Operators
'''
Identity operators are used to compare memory locations of two objects.

Operator         Description                 Example
--------         -----------                 -------
is               Identical objects           a is b
is not           Not identical objects       a is not b
'''

# Examples of Identity Operators
print("\nIdentity Operators:")
f, g = [1, 2, 3], [1, 2, 3]
h = f
print("f is g:", f is g)        # False, because f and g are different objects
print("f is h:", f is h)        # True, because h references the same object as f
print("f is not g:", f is not g) # True

#----------------------------------------------------------------------------------------------------------------------#

# 7. Membership Operators
'''
Membership operators are used to test if a value is in a sequence.

Operator         Description                 Example
--------         -----------                 -------
in               Exists in sequence          a in b
not in           Does not exist in sequence  a not in b
'''

# Examples of Membership Operators
print("\nMembership Operators:")
list_example = [10, 20, 30, 40]
print("10 in list_example:", 10 in list_example)
print("50 not in list_example:", 50 not in list_example)

#----------------------------------------------------------------------------------------------------------------------#

# Summary of Operators:
'''
1. Arithmetic: Perform mathematical operations (+, -, *, /, %, **, //).
2. Comparison: Compare values and return True/False (==, !=, >, <, >=, <=).
3. Logical: Combine conditions (and, or, not).
4. Assignment: Assign values with shortcuts (+=, -=, *=, etc.).
5. Bitwise: Perform bit-level operations (&, |, ^, ~, <<, >>).
6. Identity: Compare memory locations (is, is not).
7. Membership: Check presence in sequences (in, not in).
'''

#----------------------------------------------------------------------------------------------------------------------#
