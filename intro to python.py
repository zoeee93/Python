# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
# Using the + operator to paste together two strings can be very useful in building custom messages.
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!"）


	# list

	# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))


x[n] index n
x[start : end]     #   inclusive : exclusive    
x[:n]  # starts from index 0 to index n
x[n:]  # starts from index n  to the last index


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)


# To subset lists of lists, you can use the same technique as before: square brackets. Try out the commands in the following code sample in the IPython Shell:

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
print(x[2][0])

# results in "g"

# Replace list elements
x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]

# Extend a list
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]


In [6]: # Create the areas list and make some changes
        areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
                 "bedroom", 10.75, "bathroom", 10.50]
        
        # Add poolhouse data to areas, new list is areas_1
        areas_1 = areas +  ["poolhouse" , 24.5]
        
        # Add garage data to areas_1, new list is areas_2
        areas_2 = areas_1 + ［"garage", 15.45]
  File "<stdin>", line 9
    areas_2 = areas_1 + ［"garage", 15.45]
                        ^
SyntaxError: invalid character in identifier

In [7]: # Create the areas list (updated version)
        areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
                 "bedroom", 10.75, "bathroom", 10.50]
        
        # Add poolhouse data to areas, new list is areas_1
        areas_1 = areas + ["poolhouse", 24.5]
        
        # Add garage data to areas_1, new list is areas_2
        areas_2 = areas_1 + ["garage", 15.45]


# Delete list elements
x = ["a", "b", "c", "d"]
del(x[1])

#The ; sign is used to place commands on the same line. The following two code chunks are equivalent:

# Same line
command1; command2

# Separate lines
command1
command2

# The inner working of list； 如何避免复制一个list后，改变一个list，前一个list也改变？
# The Python code in the script already creates a list with the name areas and a copy named areas_copy. Next, the first element in the areas_copy list is changed and the areas list is printed out. If you hit Submit Answer you'll see that, although you've changed areas_copy, the change also takes effect in the areas list. That's because areas and areas_copy point to the same list.
# If you want to prevent changes in areas_copy to also take effect in areas, you'll have to do a more explicit copy of the areas list. You can do this with list() or by using [:].

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)


# help!

help(max)
?max

# Sorted

# You'll see that sorted() takes three arguments: iterable, key and reverse.

# key=None means that if you don't specify the key argument, it will be None. reverse=False means that if you don't specify the reverse argument, it will be False.

# In this exercise, you'll only have to specify iterable and reverse, not key. The first input you pass to sorted() will be matched to the iterable argument, but what about the second input? To tell Python you want to specify reverse without changing anything about key, you can use =:

sorted(___, reverse = ___)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = list(first) + list(second)

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)

# object = everything 
# methods: functions that belong to objects
# obejects of types string, float, integers, booleans and list have specific methods

# string Methods

# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()

# Print out room and room_up
print(room);print(room_up)

# Print out the number of o's in room
print(room.count("o"))

# List methods

index()
count()

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))

append()
reverse()
remove()

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)


# package


# full import
# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))


# selcetive import
# Definition of radius
r = 192500

# Import radians function of math package
  from math import radians


# Travel distance of Moon over 12 degrees and Store in dist
dist = r * radians(12)

# Print out dist
print(dist)


# Suppose you want to use the function `inv()`, which is in the `linalg` subpackage of the `scipy` package. 

    from scipy.linalg import inv as my_inv


# NumPy

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))


# height is available as a regular list

# Import numpy
import numpy as np

# Create a numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to m: np_height_m
np_height_m = np_height * 0.0254


# Print np_height_m
print(np_height_m)


# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m **2

# Print out bmi
print(bmi)


# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])


# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(np_weight[50])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[100:111])


# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)



# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])

#　i don;t fucking understand

