# tutorial: https://www.programiz.com/python-programming/type-conversion-and-casting

# PART 1

num_int = 123  # integer types can only have WHOLE numbers (no decimal values)
num_flo = 1.23  # float types can have decimal values

# Study question: what are reasons to use integers instead of floats if they have limitations?

x = num_int + num_flo

print("datatype of num_int:", type(num_int))  # prints the data type of variable num_int
print("datatype of num_flo:", type(num_flo))  # prints the data type of variable num_flo

print()  # line breaker

print("Value of x:", x)
print("datatype of x:", type(x))  # adding an integer and float creates a float

print()  # line breaker

# PART 2
# How can we print "5 + 5" using the variables "a" and "b"?

a = 5
b = "5"

# We have to cast variable "a" to a string. See below:
print(str(a) + " + " + b)  # will print "5 + 5"

# What if we want to add them together so that "a + b" gives a value of 10?
# hint: modify the below statement so that it prints 10. Try using int(...) to convert "b" into an integer type
#print(a + b)  # this will cause an error... fix it


# PART 3
# Try adding a + b (resulting in value 10) next to the following "c" string variable in a print statement
c = "Add numbers next to this string variable: "

# It's something like this, but of course, there is a bug here:
#print(c + a + b)  # should print out "Add numbers next to this string variable: 10"