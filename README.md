# Week 6

## Reading from a File
You’ll learn to handle errors so your programs don’t crash when they encounter unexpected situations. You’ll learn about exceptions, which are special objects Python creates to manage errors that arise while a program is running. You’ll also learn about the json module, which allows you to save user data so it isn’t lost when your program stops running.

```python
filename = 'data/inputData.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

```

## Writing to an Empty File
To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file. To see how this works, let’s write a simple message and store it in a file instead of printing it to the screen:

```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")  
```

### Appending to a File
If you want to add content to a file instead of writing over existing content,
you can open the file in append mode. When you open a file in append mode,
Python doesn’t erase the file before returning the file object. Any lines you
write to the file will be added at the end of the file. If the file doesn’t exist yet, Python will create an empty file for you.

```python
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```

## Exceptions
Python uses special objects called exceptions to manage errors that arise during
a program’s execution. Whenever an error occurs that makes Python
unsure what to do next, it creates an exception object. If you write code
that handles the exception, the program will continue running. If you don’t
handle the exception, the program will halt and show a traceback, which
includes a report of the exception that was raised.
Exceptions are handled with try-except blocks. A try-except block asks
Python to do something, but it also tells Python what to do if an exception
is raised. When you use try-except blocks, your programs will continue
running even if things start to go wrong. Instead of tracebacks, which can
be confusing for users to read, users will see friendly error messages that
you write.

```python
def division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as zerodv:
        print("you can not divide by Zero!")
        print(a / 1)
        print("Error: ", zerodv)
    except (NameError, TypeError) as err:
        print("please check your input!")
        raise err  # this will raise regular error message and stop your execution
    finally:  # always executed either try block or except block executed
        print("finally block is executed.")


division(45, 15)
division(45, 0)  # exception handling expected
division(45, 10)
division(45, 'hello')
division(100, 15)

```