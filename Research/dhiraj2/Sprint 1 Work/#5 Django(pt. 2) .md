# Intro to Databases

- we use databases to help develop the **backend** of our site
  - The backend is pretty much everything that the user can't see (usually data stuff)
- How do you store **data** in our projects? answer: **databases**!
  - A database is a strucutres set of data held in a computer, especially one that is accessible in various ways
  - There are many different types of databases, but we will be going over **relational databasees**
    - relational databses are made up different tables which store *records* that relate to one another (think rows and columns like and excel spreadsheet)

# SQL

> SQL allows us to utilize relational databses

SQL is short for **Structured Query Language** and is used to *manipulate* relational databses

A <u>query language</u> is different from most programming languages, in that they carry out an action for us (it does all the work on its own)

- Think of it more like a command

There are many different types of SQL (MySQL, PostreSQL, SQLite, etc.) that are all different kinds of databse management systems

- we'll be utilizing MySQL, which an open-source relational databse management system
  - We'll be using the *command-line* version, but there's also a GUI version available

# Starting MySQL

To run MySQL locally you will first need to **run the serve**

```bash
mysql.server start
```

Then you login to MySQl using:

```bash
#the default root username has no password, but you should change that for security
mysql -u <username> -p <password
```

* `mysql -u root` will work for the first time login

# Using the database

`SHOW DATABASES;` will display all databases

`CREATE DATABASE <database_name>;` creates database with <databse_name>

`USE <database_name>;` selects the database that we're going to use

`DROP <databse_name>;` will *permanently delete the databse*

# Interacting w/ tables

## Table manipulation

`SHOW TABLES;` displays all the tables in the databse

`CREATE TABLE <table_name>(<columns>);`  will create a table ith <table_name> and with the columns specified

- Example: 

  ```mysql
  CREATE TABLE students (
  	unin int NOT NULL,
    FirstName varchar(255),
    LastName varchar(255),
    StudentInCS196 BIT,
    Primary Key (uin)
  );
  ```

`DROP TABLE <table_name>;`  wil *permenently delete the table*

`DESCRIBE <table_name>;` displays the **schema** (how the table is organized) of a table

## Querying Tables

The query, we use the SELECT - FROM - WHERE pattern

```mysql
#WHERE is optional
SELECT <columns> FROM <table_name> WHERE <condition>;
#To get all columns from a table
SELECT * FROM <table_name>;
#do get get some columns
SELECT col1,col2 FROM <table_name>;
#To get all the columns that meet a condition:
SELECT * FROM <table_name> WHERE <condition>
```

# MySQL vs Django Models

> In practice, working with databses is a little more redious that just writing the easy SQL commands
>
> You have to connect to the databse server, manually create all those tables, use JS or PHP to run SQL commands, and it all gets very tedious

Instead of working with the databse directly by writing tedious commands, we can use **Django Models** to carry all of this out for us

A **Djando Model** is like a *class* in your code, and the *objects* you create are actually **records** in your tables

- A **class** is a template for creating **objects**
- Django handles all the nitty gritty details of actually transferring this information over to your databse

# Using Django Models

## models.py

*remember our SQL schema from before?* let's recreate that as a model in a file called `models.py`

`hello_world/models.py`

```python
from django.db import models

#Create your models here
class Students(models.Model):
  Uin = models.IntegerField(default=0)
  FirstName = models.CharField(max_length=255)
  LastName = models.CharField(max_length=255)
  StudentInCS196 = models.BooleanField(default=False)
```

## settings.py

*before we can add this table, we have to edit our settings.py file and add our class to the installed apps*

`settings.py`

```python
INSTALLED_APPS = [
  'hello_world',
]
```

*We also have to edit our databses section in order to use a databse*

```python
DATABASES = [
  'default': {
    'ENGINE': 'django.db.backend.mysql',
    'NAME': 'cs196lecturedjango', 
    'HOST': '127.0.0.1',
    'USER': 'root',
    'PASSWORD': '',
  }
]
```

## Migrating our changes

To finally add the table, we run run these commands in to root directory of our project:

```bash
python3 manage.py makemigrations
```

then run

```bash
python3 manage.py migrate
```

# Django Admin

> Djando Admin will handle a lot of the SQL stuff for us, so let's use it!

If we run our changed project and navigate to `<host_name>/admin/` we will see a *login* screen!

*But,* we need to create an admin user first!

<u>In the root directory of the project run this command</u>

```bash
python3 manage.py createsuperuser
```

- fill out the info and you're ready to go!

*However,* nothing shows up on our admin page! To change this, let's create an admin.py file in our project!

## admin.py

`hello_world/admin.py`

```python
from django.contrib import admin
from .models import Students

#register your models here
admin.site.register(Students)
```

Now we can direstly manipulate the databases :thumbsup:

# Programmatically Manipulate Information

> How can we programmatically manipulate this information instead of using the admin page?

## Adding records

### views.py

we need to edit our views to add stuff 

`hello_world/views.py`

```python
from .models import Students

#Create your views here
def home(request):
  #values for our new student
  uin_new = 1234
  FirstName_new = "Ichigo"
  LastName_new = "Kurosaki"
  StudentInCS196_new = 0
  #creating a new student
  new_student = Students(Uin=uin_new, FirstName = FirstName_new, LastName = LastName_new, StudentInCS196 = StudentInCS196_new)
  #saving it
  new_student.save()
  
  #return the full name to html file
  return render(request, 'index.html', {'name':FirstName_new})
```

## Getting Records

### views.py

```python
  #saving it
  new_student.save()
  
  #we can get the uing using
  retrieve_student = Students.objects.get(Uin=uin_new)
  #then we can use that, since its the key to get the other values
  full_name = retrieve_student.FirstName + " " + retrieve_student.LastName
  
  #return the full name to html file
  return render(request, 'index.html', {'name':full_name})
```

