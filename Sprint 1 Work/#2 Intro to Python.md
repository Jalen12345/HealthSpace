# What is Python?

- Its a progrmaming langauge
  - Interpreted
  - Object-oriented
  - High-level programming
- Python files will have a `.py` file extension
- Code is desinged to be highly readable and concise

# Python Coding

## Printing

You can print out a string to the console by using `print()`

```python
print("Hello World!")
#print w/out new line
print("Hello World!", end="")
```

## Variables

- Variable help up store **stuff** in our programs
  - we can store more than just 'data'
- Python has **Dynamic Typing** so we don't need to specify a type from declaring a variable (it's smart enough to figure it out!)
  - Many different datat types such as integers, floats, strings, booleans, etc.
- The **None** type is often used as an empty placeholder since you can't manipulate the NoneType

```python
# x as an integer
x = 4
# x as a list of integers
x = [1, 2, 3, 4]
# x as a string
x = "im a chamelon"
```

## Conditionals

- conditionals let you make decisions in your code!
- operators
  - `==`  
    - true if values are the same
  - `!=`
    - true if values are not the same
  - `>=` `<=` `>` `<`
    - checks if the relative values meet the crieria
  - `is`
    - checks if referencing the same object
  - `in`
    - checks if value is within another object

- you can have compound conditionals using the `and` or `or` keywords to combines 

Sample Code:

```python
#Getting input from the user and storing it in x (as a string)
x = input("What number should x be: ")
#casting that string to an int since it is a number
x = int(x)
#Checking what x is and then deciding what to do
if x == 196:
	print("Hey that's the number of this class!")
elif x % 2 == 0:
  print("Your number is even!")
else:
#you can pass in variables to the print function
	print("You typed in ",x)
```

## Loops

- Loops allow us to **repeatedly run** the same section of code
- We will cover how to use **for loops** and **while loops**

### For Loops

```python
#will iterate from 0 to 9
for i in range(10):
	print(i)
#will iterate from 2 to 9
for i in range(2,10):
  print(i)
#will iterate from 2 to 9, counting by 2. output = (2,4,6,8)
for i in range(2,10,2):
  print(i)
x = ["H","E","L","L","O"]
#will iterate across each element in a data structure
for i in x:
  print(i)
```

### While Loops

- Will continue to iterature while any given statement is `True`

```python
x = 100
while x > 50:
	print(x)
	x -= 1
```

- you can also use the `break` keyword inside an if statement to terminate your loop if a given condition is met

## Functions

- A function is a block of code that we plan on reusing
- Instead of writing the ame code over and over we can write a function and call it!

```python
def greet(name, time):
	if time == 'm':
		print("Good Morning, ",name)
	elif time == 'a':
		print("Good night, ",name)
	else:
		print("Hello, ",name)
```

### Return

- A function will return to the code that called it once the function has finished running
- If we want to manually leave a fucntion we can use the return keyword

```python
#Returning a value
def isEven(number):
	return number % 2 == 0
	
result = isEven(5)

#returning multiple values
def test():
  x = 1;
  y = 2;
  return x, y

a, b = test()

```

## Lists

- List are a collection which is **ordered** and **changeable**
- duplicate values are allowed
- <u>List != Arrays</u> because lists are resizeable
- uses `[ ]` 
  - can put in index or range
    - `[2:5]` to get from range 2 to 5 or `[2:]` to get from 2 onwards or `[:2]` to get range from 0 to 2
- String are lists
- Other functions:
  - `.append(x)` will add the item to end of the list
  - `.insert(index, x)` will add the item at the index, pushing everything after it over
  - `.remove(x)` will remove the first occurance from the list
  - `.pop()` will return the first element and delete it from the list
  - `.reverse()` will reverse the list
  - `.sort()` will sort the list

# Exception Handling

- when an **exception** (error) ocurs, Python will stop running and send us an error message - not a graceful exit
- So, we use **exception handling** to handle exceptions without crashing the program
- To do this we use the `try` `except` and `finally` commands
  - if an excpetions occurs in the `try` block, Python catches the excpetion and moves onto the except block and runs the in there
  - The code in the `finally` block wil be run regardless, so its more an **optional** step since you can right you code outside 

```python
def test():
	x = "Hi"
	try:
		x += 1
	except:
		print("trying to add an int to a string :(")
		return
#test will print out "trying to add an int to a string :("		
test()
```

**<u>*N.B*</u>** : an *if-else* always has a cost to do that comparison, while a *try-except* has a minimal cost, **however** is an exception does occur it is very costly

# Pythonic Code

- There's usually a very clearn way to do things in python
- Don'tbe afraid to look up how to do things!

# More w/ Lists

## List Comprehension

Uses an `Output Expression` then an `Input Sequence` an an optional `Predicate`

Example:

```python
squared = [n ** 2 for n in list if type(n) == types.IntType]
```

## Enumeration

- Will assing each value in the list a number (it is a function)

Example:

```python
foods = ["pizza", "kimchi","ramen"]
for i, food in enumerate(foods):
	print(i, food)
#result will be: 0 pizza 1 kmichi 2 ramen
```

# Sets

- unordered and unindexed
- each value is **unique**
- Very fast used as a lookup table
- has functions to get what you'd see in 'Math Sets'
  - Union
  - Intersection

Example

```python
numSet = set([1,2,2,3,4,4,5])
```

- Can use `.union(otherSet)` to combine two sets and `.interesect(otherSet)` to find the numbers that appear in both sets

# Dictionary

- Uses **Key - Value** pairs
- Very vast when used as a lookup table (just like a set!)
- 

Example:

```python
#Making a dictionary
car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#Accessing Values:
print(car_dict['brand'])
#alternative notation
print(car_dict.get('brand'))

#looping through values in dictionary

#using keys
for key in car_dict:
  print(key)
#using values
for value in car_dict.values():
  print(value)
#using both
for key, value in car_dict.items():
  print(key, value)
```

N.B. => if you use .get on a key that doesn't exist, it will return `None`, while if you use the [ ] notations is will raise a `Key Error`

