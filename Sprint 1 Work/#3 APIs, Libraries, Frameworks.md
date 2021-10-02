> Good programmers are *lazy*

# Libraries v.s. Frameworks

| Libraries                                                    | Frameworks                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Provides a set of helper function/objects/modules which your application code calls for specific functionality | Defined open or unimplemented function or objects which the user writes to create a custom applications. (more like a 'skeleton') |

# Steps to take

1. Research
   - Google what you need
   - Match your intentions to the least amount of work
   - Collect a few candidates
2. Evaluate
   - How does it look?
3. Try it out
   - Try to experiment with it to see how you feel about it
   - (make sure you do this experimenting on a new branch)
4. Tie it in
   - Put the ingredient into the melting pot

# What makes a library good?

1. **Github stars** : Quite simply, the more the better. Think of these as how people say they 'like' the library
2. **README** : look at the readme to learn more about it
3. **Docuemtnation** : skim through it, does it seem like everything is well documented and easy to the understand? is there example code?
4. **Support** : Look as the issues, can you find the help you need?

# Implementation in Python

In order to bring functions into our program for our own usage, we have to use `import`

## import

you can import:

- **Modules**: simply a file with a .py extension
- **Package:** a directory containing an `__inint__.py` file and normally other modules
- **Built-in Modules** a module that is natively installed with Python
- **Object**: Anything inside a module/package that can be references such as class, function, or variable

### How to import

- To import an *entire* module/package

  - **Synatx:** import <module/package>

  - Example:

    ```python
    #importing the math library
    import math
    #can call a function using the library name and dot notation for the function
    x = math.factorial(6)
    print(x)
    ```

  - However, this isn't very efficient

- To import *only the stuff you need*

  - **Syntax: ** from <module/package> import <stuff>, <stuff>

  - Example:

    ```python
    #importing the the two functions we need from math
    from math import gcd, factorial
    #we can call these functions w/out the math prefix
    print(gcd(26,10))
    print(factorial(5))
    ```

- To rename:

  - **Synatx:** as <new name>

  - Example

    ```python
    #renaming factorial as fact
    from math import factorial as fact
    #using it with the assigned name
    print(fact(5))
    ```

***<u>However, when people write libraries, they use other libraries</u>***

# Package Managers

- To solve the problem of libraries needing other libraries and so on, we use a package manager to handle all this stuff for us

## pip

- Pythons package manager is called pip
- To install a pakcage you do `pip install <package name>`
- If you want to get all the packages you need to run your code
  - use a `requirements.txt` file that lists all the libraries and their version so you can download them all using `pip install -r requirements.txt`

# APIs

**A**pplications **P**rogramming **I**nterfaces

## The basics

- APIs allow the client(you) to send requests to the server and then get the result back
  - Example: using google map's API in order to implement a map

## HTTP

**H**yper**T**ext **T**ransfer **P**rotocol

- Designed to allow for communication between clients and servers

![HTTP_RequestMessageExample](https://documentation.help/DogeTool-HTTP-Requests-vt/http_requestmessageexample.png)

### Methods

- `GET`
  - Used to <u>get</u> data data from a specifies course
  - The **query string** is in the URL of the GET request
  - `GET <url><query_string>`
  - **Query String Syntax:** `?name=ferret&color=purple`
  - GET requests should never be used when dealing w/ sensistive info
  - GEt request can only request data (can't modify)
- `POST`
  - used to <u>post</u> (send) data to the serve to create or update records
  - Data sent to a server via post is **stores in the body** of the HTTP request
  - POST is a little safer than GET
- `PUT`
- `DELETE`

## Data

### Data Representation

| JSON - JavaScript Object Notation    | XML - Extensible Markup Language           |
| ------------------------------------ | ------------------------------------------ |
| Similar to dictionaries              | Older format                               |
| Standard for serializing data object | not as popular                             |
| Popular                              | nested structure                           |
| Nested Structre                      | made up of chunks of data called **nodes** |
| Uses key-value pairs                 |                                            |

### JSON

#### Structure

- JSON string are made up of **objects** and **arrays**
- **Array** - surrounded by `[ ]` and contianed a comma separated list of values
- **Object** - surrounded by `{ }` and continas a comma separates list of *key-value pairs*
- **Key-Value Pairs** -  in the format of `"<key>":<value>`

#### Data Types

Values in an object/array can be:

- Integers
- Floating points
- String (surrounded by double quotes)
- Booleans (true or false)
- Nested array
- Nested object
- NULL value

#### Example

```json
{
	"name": "John Doe",
  "uin": 123456789,
  "classes": {
    {
    	"class_name": "CS196",
    	"grade": "A"
  	}
  }
	"FLR Complete" : true
}
```

> You can use https://reqres.in/ if you want practice with APIs and test them out

## Making Requests in Python

1. Find API, and read its **documentation**
2. You'll probably need to get an API key
3. Generate a URL from the API documentation 
4. Test your request either in your browser or using a tool like Postman
5. Integrate it inot your program