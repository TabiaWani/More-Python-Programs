# Arithmetic expressions
a = 10
b = 3

addition = a + b       # 10 + 3 = 13
subtraction = a - b    # 10 - 3 = 7
multiplication = a * b # 10 * 3 = 30
division = a / b       # 10 / 3 = 3.333...
modulus = a % b        # 10 % 3 = 1 (remainder)
exponent = a ** b      # 10^3 = 1000
floor_division = a // b # 10 // 3 = 3 (integer division)

print("Addition:", addition)
print("Floor Division:", floor_division)
print("multiplicatio:,", multiplication)
print("subtraction:", subtraction)
print("division:", division)
print("modulus:", modulus)
print("exponent:",exponent)

# Membership expressions
text = "Python"
print("P" in text)      # True ('P' is in "Python")
print("z" not in text)  # True ('z' is not in "Python")

nums = [1, 2, 3, 4]
print(3 in nums)        # True (3 is in the list)
print(5 not in nums)    # True (5 is not in the list)

# Identity expressions
a = [1, 2, 3]
b = a  # Both refer to the same object
c = [1, 2, 3]  # Different object with the same values

print(a is b)        # True (same object)
print(a is c)        # False (different objects)
print(a is not c)    # True
print(b is not a)


#bitwise operators
x = 5   # Binary: 0b0101
y = 3   # Binary: 0b0011

print(x & y)  # AND operation
print(x | y)  # OR operation
print(x ^ y)  # XOR operation
print(~x)     # NOT operation (bitwise inversion)
print(x << 1) # Left shift by 1
print(x >> 1) # Right shift by 1



