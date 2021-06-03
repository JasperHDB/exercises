# Samenvatting

## 1. Loops

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

## 2. Date Parsing (door Jesse)

Nog een PSA voor de date parsing, als je geen leading zero's wilt hebben (e.g 01/02/2021) en als je datetime.strftime() gebruikt; dan moet je dit doen:

```python
datetime.strftime(date, "%#d-%#m-%Y")
```

## 3. Scripting

### 3.1 Parameters

Parameters are made available to the script through the `sys.argv` array.

```python
import sys

print(" ".join(sys.argv[1:]))
```

### 3.2 Reading a file

I/O, i.e., reading data from and writing data to the external world, is a core aspect of scripting. Typical examples are files and network sockets.

```python
import sys

with open(sys.argv[1], 'r') as file:
    print(file.read())
```