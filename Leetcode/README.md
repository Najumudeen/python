#######################################
#                                     #
# Shallow Copy Vs Deep Copy in Python #
#######################################

In Python, Assignment statements do not copy objects, they create bindings between a target and an object.

a = [1, 2]

b = a

a ===> [1, 2]  <==== b

## Copy
### Shallow Copy

What is Shallow Copy?

shallow copy doesn't copy objects recursively. it creates a copy of the main object on which the copy function was called,
and if that object contains other objects. In shallow copy we use the same references of those objects instead of creating new objects for them as well.

## Shallow Copy

import copy

ls = [1, 2, [3, 5]]

ls2 = copy.copy(ls)

# Append 6 to ls

ls.append(6)

print(ls)

print(ls2)

# Append 7 to the inner list
ls[2].append(7)

print(ls)

print(ls2)

What is deep Copy?

Deep Copy is a process in which the copying process occurs recursively. it means first constructing a new collection object and then
recursively populating it with copies of the child objects found in the original.

In case of deep copy, a copy of object is copied in other object. it means that any changes made to a copy of object do not reflect in the original object. in python, this is implemented using "deepcopy()" function.

### Deep Copy
ls = [1, 2, [3, 5]]

# Shallow Copy
ls2 = copy.deepcopy()

# Append 6 to ls
ls.append(6)

print(ls)

print(ls2)


# Append 7 to the inner list
ls[2].append(7)

print(ls)

print(ls2)

################################END######################


what is monkey patching?

#######
diff between == and is operator in python

in Python, == checks for equality

if we have two objects a and b, a == b checks if both a and b are equal

__eq__ method

li1 = [1, 2, 3]
li2 = [1, 2]

li1 and li2 is a place holder.

print(id(li1))
print(id(li2))

values are same but object are different

what does 'is' check for ?

In Python, the is operator check for identity.

In simple terms 

li1 is li2

Flase

li2 = li1

#########
# How many ways can we use underscore in python?
# How to declare a private variable in Python?
# Explain about the different access modifiers in Python?
# what is Name mangling?

We are going to discuss about all these questions in details in the upcoming 3 videos.

How many different ways underscores (_) are used in Python?

_: single underscore

1. In Interpreter, _ can be used to get the output of the last executed cell.
2. In a program, it can be used to signify that a value does not hold significance.
   For example, it can be used when we run a for loop for a set number of times, but do not need to store the 
   iteration numbner in any variable.

_var: Single Leading underscore in variable/method name

The single underscore prefix has a meaning by convention only.

The underscore prefix is meant as a hint to another programmer that a variable or method starting with a single
underscore is intended for internal use. This convention is defined in PEP 8.

var_ : Single traling underscore in variable/method name

__var: Double leading underscore in variable/method name


The closest to a private variable or method you can have in python.

Having a dunder before a varible name, tells python interpreter to rename the particular variaable so that it can not 
be called directly from another class or progeam.

The process of changing the name is called "Name mangling"

__var__ : Double Leading and Traling underscores in variable/method name

However, names that have both leading and traling double underscores are reserved for special use in the language. This
rule covers things like __init__ for object constructors, or __call__ to make an object callable.

These dunder methods are often referred to as magic methods

Examples of magic methods: __init__, __call__, __eq__, __it__, __gt__ etc.

dir(int)


In the last video we talked about:

In how many ways can we use underscore in python?

What are access modifiers and How are they implemented in Python?

    the access to class resources like(variables, members etc)

    Using the 3 most common access modifers - Public, Protected, Private

    a developer can control the access to class resources very easily.

3 Scenarios:

  1. Class members can be accessed from any subclass or outside the class.
  2. Class members can be accessed with in the same class and sub classes.
     But not from outside the class
  3. Class members can be accessed only from within the class. Not from anywhere else.


Public Access Modifiers.

   Public access modifiers allows the class member to be accessed from anywhere.
   it can be accessed from within the class, from subclasses of the class and from classes that 
   exist in another pacakge altogether.


In the next video we talked about Private variables in Python? what is Name mangling?

Traditionally, if you declare a class member as protected, you can access it from that class itself and it's subclasses.
But cannot be accessed from any other class that is not a subclass.

Python does not support protected access modifiers as a language feature.
But there is a convention of using (_varname) to indicate that it is a class member that is meant for internal uses only.
A responsible developer is not going to use that member directly in any other class, but rather wiuld take the help of a getter, setter priperty.


Private variable are class members that cannot be accessed from any where outside the specific class where the member is defined.

(__varibale)  (__functionname)

not access the above to 