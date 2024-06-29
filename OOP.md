# An object is a container for variables and functions

# Variables | Health , Energy, Stamina, Damage 
# Functions | Attack, Movement, Animations

Special names only for OOP
# Variables - > Attributes
# Functions - > Methods


# A class is the blueprint for an object

- Classes precedes objects
- A class also accepts arguments to customise the object

Why use classes and objects?
1. They organise complex code
2. They help to create reusable code
3. They are used everywhere
4. Some modules require you to create classes
5. They make it easier to work with scope

# A dunder method is a method that is not called by the user
 - Instead, it is called by python when something happens

- Everything in python is an object

# A `function` and a `method` both execute a block of code

- The difference is that a method belongs to an object

                `function`         `method`
                len('test')        test.upper()  
    - can be used by others        - only works for string
                     

# print(dir(test)) - you get objects 

# Inheritance means that 1 class gets attributes and methods from another class (or classes)

- A class can inherit from an unlimited number of other classes
- A class can also be inherited from by an unlimited number of classes

Inheritance, can get very complex
- However, most of the time you just need simple inheritance

# Private attributes
- Cannot be changed ( Convention only )
# self.id = 5

# hasattr(object, 'attribute') - True or False
- hasattr(monster, 'health')

# setattr(object, 'attribute', value)
- hasattr(monster, 'weapon', 'Sword')
- print(monster.weapon) , output : Sword

# help()