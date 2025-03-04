#----------------------------------------   Bytes and Bytearray in Python   -------------------------------------------#
#                                        -----------------------------------

"""
In Python, `bytes` and `bytearray` are used to handle binary data. They represent
sequences of bytes (8-bit values). These types are particularly useful for working
with binary files, network data, or other non-textual information.

- `bytes`: Immutable sequence of bytes.
- `bytearray`: Mutable sequence of bytes.
"""

# Key Points about Bytes and Bytearray:
'''
Bytes:
- Immutable: Once created, cannot be modified.
- Used for binary data like images, files, etc.

Bytearray:
- Mutable: Can be modified after creation.
- Useful when working with binary data that needs to be changed.

Both can only contain integers in the range 0–255.
'''
#----------------------------------------------------------------------------------------------------------------------#

# 1. Creating Bytes
bytes1 = b"Hello"  # Using a bytes literal with `b` prefix
bytes2 = bytes([72, 101, 108, 108, 111])  # From a list of integers
bytes3 = "Hello".encode('utf-8')  # Encoding a string to bytes

print("Bytes 1 (literal):", bytes1)
print("Bytes 2 (from list):", bytes2)
print("Bytes 3 (encoded string):", bytes3)

# 2. Creating Bytearray
bytearray1 = bytearray(b"Hello")  # From a bytes object
bytearray2 = bytearray([72, 101, 108, 108, 111])  # From a list of integers

print("\nBytearray 1 (from bytes):", bytearray1)
print("Bytearray 2 (from list):", bytearray2)

# 3. Accessing Bytes and Bytearray
'''
Both `bytes` and `bytearray` are sequences and support indexing and slicing.
'''
print("\nFirst byte in Bytes 1:", bytes1[0])  # Access first byte (72 = ASCII 'H')
print("Slice of Bytearray 1:", bytearray1[1:4])  # Access slice (b'ell')

# 4. Modifying Bytearray
'''
Since `bytearray` is mutable, its contents can be changed.
'''
print("\nOriginal Bytearray 1:", bytearray1)
bytearray1[0] = 74  # Change the first byte to 74 (ASCII 'J')
print("Modified Bytearray 1:", bytearray1)

# 5. Methods for Bytes and Bytearray
'''
Both `bytes` and `bytearray` support many common methods, such as:
- `decode()`: Convert bytes to string.
- `count()`: Count occurrences of a byte.
- `find()`: Find a byte's index.
'''

# Decoding bytes to string
decoded_string = bytes1.decode('utf-8')
print("\nDecoded Bytes 1 to String:", decoded_string)

# Counting occurrences
count_l = bytes1.count(b'l')  # Count 'l' in bytes
print("Count of 'l' in Bytes 1:", count_l)

# Finding index
index_e = bytearray1.find(b'e')  # Find 'e' in bytearray
print("Index of 'e' in Bytearray 1:", index_e)

# 6. Appending to Bytearray
'''
New bytes can be added to a `bytearray`.
'''
print("\nOriginal Bytearray 2:", bytearray2)
bytearray2.append(33)  # Append 33 (ASCII '!')
print("Bytearray 2 after Append:", bytearray2)

# 7. Converting Between Bytes and Bytearray
'''
Conversion between `bytes` and `bytearray` can be done using the respective constructors.
'''
converted_bytes = bytes(bytearray2)  # Convert bytearray to bytes
converted_bytearray = bytearray(bytes1)  # Convert bytes to bytearray

print("\nConverted to Bytes:", converted_bytes)
print("Converted to Bytearray:", converted_bytearray)

# 8. Iterating Over Bytes and Bytearray
'''
You can iterate over `bytes` or `bytearray` to process each byte.
'''
print("\nIterating Over Bytes 1:")
for byte in bytes1:
    print(byte, end=" ")  # Print each byte value

print("\n\nIterating Over Bytearray 1:")
for byte in bytearray1:
    print(byte, end=" ")

# 9. Using Memoryview
'''
A `memoryview` object can be used to access the binary data of `bytes` or `bytearray` without copying it.
This is useful for handling large binary data.
'''
memview = memoryview(bytearray1)
print("\n\nMemoryview of Bytearray 1:", memview)
print("First byte from Memoryview:", memview[0])

# 10. Comparison of Bytes and Bytearray
'''
 ____________________________________________________
| Feature         | Bytes       | Bytearray          |
|-----------------|-------------|--------------------|
| Mutability      | Immutable   | Mutable            |
| Usage           | Read-only   | Modifiable         |
| Example Usage   | Network data| Image manipulation |
 ----------------------------------------------------
'''

#----------------------------------------------------------------------------------------------------------------------#
