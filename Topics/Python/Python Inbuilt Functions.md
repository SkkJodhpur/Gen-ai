Python provides a rich set of inbuilt functions that are readily available for use without needing to import any additional modules. These functions perform various tasks such as data type conversions, mathematical operations, handling sequences, etc. Here's a categorized list of some commonly used Python inbuilt functions:

### 1. **Type Conversion Functions**
   - `int()`: Converts a value to an integer.
   - `float()`: Converts a value to a float.
   - `str()`: Converts a value to a string.
   - `bool()`: Converts a value to a Boolean (`True` or `False`).
   - `list()`: Converts a sequence to a list.
   - `tuple()`: Converts a sequence to a tuple.
   - `set()`: Converts a sequence to a set.
   - `dict()`: Converts a sequence to a dictionary.

### 2. **Mathematical Functions**
   - `abs(x)`: Returns the absolute value of a number.
   - `round(x[, n])`: Rounds a number to the nearest integer or to the specified number of decimal places.
   - `min(iterable, *args)`: Returns the smallest item in an iterable or the smallest of two or more arguments.
   - `max(iterable, *args)`: Returns the largest item in an iterable or the largest of two or more arguments.
   - `sum(iterable, start=0)`: Sums the items of an iterable, starting with a given value (default is 0).
   - `pow(x, y)`: Returns `x` raised to the power of `y`.

### 3. **Sequence and Iterable Functions**
   - `len(s)`: Returns the length (number of items) of an object.
   - `range(start, stop[, step])`: Generates a sequence of numbers from start to stop with a step.
   - `sorted(iterable, *, key=None, reverse=False)`: Returns a new sorted list from the items in an iterable.
   - `reversed(seq)`: Returns a reverse iterator over the values of a sequence.
   - `enumerate(iterable, start=0)`: Returns an enumerate object. It adds a counter to an iterable.
   - `zip(*iterables)`: Aggregates elements from each of the iterables.

### 4. **Input/Output Functions**
   - `print(*objects, sep=' ', end='\n', file=sys.stdout)`: Prints objects to the text stream file.
   - `input(prompt=None)`: Reads a line from input, converts it to a string (stripping a trailing newline), and returns it.

### 5. **Object and Variable Handling**
   - `type(object)`: Returns the type of an object.
   - `isinstance(object, classinfo)`: Checks if an object is an instance of a class or a tuple of classes.
   - `id(object)`: Returns the identity of an object.
   - `dir([object])`: Without arguments, returns the list of names in the current local scope. With an argument, returns a list of attributes of the object.

### 6. **File Handling Functions**
   - `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`: Opens a file and returns a corresponding file object.
   - `close()`: Closes an open file.
   - `read([size])`: Reads data from a file.
   - `write(string)`: Writes a string to a file.

### 7. **Utility Functions**
   - `help([object])`: Invokes the built-in help system.
   - `eval(expression)`: Evaluates a Python expression from a string-based input.
   - `exec(object[, globals[, locals]])`: Executes dynamically created Python code.
   - `any(iterable)`: Returns `True` if any element of the iterable is true.
   - `all(iterable)`: Returns `True` if all elements of the iterable are true.

### 8. **Miscellaneous Functions**
   - `hash(object)`: Returns the hash value of an object.
   - `globals()`: Returns a dictionary representing the current global symbol table.
   - `locals()`: Returns a dictionary representing the current local symbol table.
   - `callable(object)`: Returns `True` if the object appears callable, `False` if not.
   - `format(value, format_spec='')`: Returns the formatted representation of a value.

These functions cover many of the common needs you'll encounter when writing Python code. If you need functionality beyond these built-in options, Python also provides a vast standard library and the ability to install third-party packages.

Link: https://docs.python.org/3/library/functions.html
