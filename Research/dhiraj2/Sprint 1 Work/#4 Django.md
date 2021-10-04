> READ THE **DOCUMENTATION**

# What is a web framework?

- web frameworks are **software frameworks** that we use to help us make **web applications** like
  - web services
  - web resources
  - Web apis

## Why Django?

- **Security** - Popular frameworks have the benefit of large communities which can quickyl fix bugs
- **Efficiency** - you can rapidly develop applications by utilizing ready-made functionality within the framework instead of rewriting hundreds of lines of code yourself
- **URL Mapping** - It's very easy to index multiple pages and make them easily accessible
- **Cheap** - The most popular frameworks are free and you can develop faster (time == money)
- **Support** - Extensive documentation, support team, community forums, etc. will provide loads of support that makes learning super easy
- From django website:

> Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experiences developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source

# Model-View-Controller

- The **model-view-controller (MVC)** is a software design patter used for developing user interfaces
- The program logic is split inot the tree interconnected elements
- this levevl of abstraction is done to separate the back-end from what is used by the user

### Model

handles all data log - storage, retrieval, logic, etc.

### View

handles all visual/UI components, it uses data received from the model (from the controller) to display information to the user

### Controller

handles all user interactions and then sends commands to the model and view to update based on user input

## How it works

1. The computer makes a request to the **controller**
   - A **Controller** will handle request flow (not data logic)
2. the Controller gets data from the **model**
   - a **Model** handles data logic and interacts with the database
3. then the **controller** uses the data is got from the **model** and sends it to the **view** in order to recieve make the presentation
   - a **View** handles data presentation and is dynamically rendered
4. The **controller** gives back the presentation it got from the **view** and sends it back to the computer as a response

## MVT vs MVC

- a lot of popular frameworks use/are based on MVC:
  - AngularJS
  - EmberJS
  - Rails
- Django's MVT pattern is similar enough to the MVC pattern to be called MVC
  - the Controller is handled by the framework itself
  - We use **templates**, which are static HTML and CSS couples with special syntax to create dynamic elements

# Django Setup

## Installing

```bash
pip install Django
```

- you can run `django-admin --version` to see whether Django installed correctly

If you are planning yo have a **database** then we should make sure we have what we need for that as well

- MySQL for example

N.B. => Some people recommend setting up a **virtual environment before starting a project **

- Especially easier if you're dealing with multiple projects 

# Getting Start w/ Django

## Step 0 - Folders

1. Create a project folder `mkdir <project_folder_name>`
2. Move into folder `cd <project_folder_name>`

## Step 1 - Creating a project

1. run `django-admin startproject <project_name>`
   - Now django will create out project for us in folder with `<project_name>`
2. `cd` into that folder. We sould see *two* things in here:
   1. A file called **manage.py**
   2. Another folder with the name `<project_name>`
3. To check that everything is running properly run this (you also use this command to start running your project)
   - `python manage.py runserver`
4. If a browser doesn't automatically open up, then you can open a window and navigate to http://127.0.0.1:8000

# Web Tech Basics

*With <u>static</u> websites we use*

- **HTML** : Hyptertext Markup Language, which can create pages that are displayed on the web
- **CSS** : Cascading Style Sheets, which can describe the presentation of markup languages like HTML
- **JavaScript** : Allows us to se **client-side scripting** to create dynamic pages

*Static Websites*

- Website that show the same thing to everybody
- b o r i n g 

*Dynamic Webistes*

- Can be **tailored** to the use
- **Updated** with new information
- **Django** (and other frameworks) make it really easy to create dynamic websites
- Our **template** will use HTML-CSS-JS

# Django Project Strucutre

```bash
#The root directory that Django creates
[projectname]\
#the actual Python packaage for this project (use this when importing anything)
	[projectname]\this directory can be treated like a package
	#empty file that let's python know 
 		__init__.py
 	#Stores all the setting/configuration for our project
		settings.py
	#lets us do our URL mappings(index for all our pages)
		urls.py
	#Web Server Gateway Interface is the standard used to communicating w/ web servers
		wsgi.py
#command line utility that let's you interact w/ Django project
	manage.py
```

# Dynamic 'Hello World' Example

Let's start by creating our hello_world app

```bash
python manage.py startapp hello_world
```

- This will create a `hello_world` folder which will be our **application**

Next, we'll create a `urls.py` file to help us index all our pages and provide the relevant mappings to all these pages

## urls.py (in the hello_world directory)

```python
from django.urls import path
from . import views

urlpatterns = [
  #when the url has nothing ('') we want to view the home page
  path('', views.home, name="home")
]
```

Next we'll need to create a file called `views.py` that has this home function that we're calling

## views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

#Create your views here
#When we get a request (from the controller)
def home(request):
  #return an HTTP Response of hello world
  return HttpResponse("Hello World")
```

> **HOWEVER** this doesn't work completey, because the `urls.py` file we creates doesn't handle the mapping for our entire project, only the `urls.py` in the *root* directory does
>
> *So* we need to let the `urls.py` in the root directory know about the `hello_world/urls.py`

## urls.py (in the root directory)

The original file looks like this:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
  path('admin/', admin.site.urls),
]
```

We should update it to look like this:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('',include('hello_world.urls')),
]
```

> **BUT WAIT**, this isn't dynamic yet, it just displays hello world! (boring)

## Using Templates

<u>To create large dynamic pages we will use **templates**, which are written using HTML/CSS/JS and use the Django Template Language to become *dyanmic*</u> 

First let's make a folder called template in our **root** directory

Next we need need to update our `settings.py` so that it knows where to pull the templates from

```python
#in the settings.py file there should be a line that looks like this:
'DIRS': [],
```

```python
#we should add our directory 
'DIRS': [os.path.join(BASE_DIR, '<name_of_template_folder>')].
```

Then, we'll create an HTML *inside* of your templates folder

- You can add anything, but for simplicity we'll just be doing

```html
<h1>
  Hello, World! But from a ~file~
</h1>
```

Then, we'll update our `hello_world/urls.py` to render our HTML file

```python
def home(request):
  return render(request, 'index.html')
```

> This is cool! But we still need to make it dynamic!

## Making it dynamic

We want to render a dynamic variable within our app using Django Template Library

in **hello_world/views.py**

```python
def home(request):
  return render(request, 'index.html',{'name':'CS 196 Student'})
```

- Variables use the notation

  'var_name' : value

Finally you can pass this into the html file using {{}}

```html
<h1>Hello {{name}}, how's it going?</h1>
```

