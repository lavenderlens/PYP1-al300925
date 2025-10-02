'''
a class is
a BLUEPRINT or TEMPLATE for
creating objects of a certain user-defined type
there exist many system classes such as str and list
when we create our own classes, however, we create our own types
you may choose classes over dictionaries to represent complex data
as every instance of the class will have 
the same fields (variables) and
the same methods (functions)
whereas if we used dictionaries, every usage has to be defined again
classes enforce standards applied by all objects of that class
they may also restrict direct access to state variables (data hiding/encapsulation)

also, classes may INHERIT from other classes
ensuring less code duplication
'''
class Client:
    pass

client = Client()#RHS completes and is only then assigned to the LHS variable
print(client)#<__main__.Client object at 0x10041a900> / 0x104b36900> - volatile memory address
# print(client.prop)#AttributeError: 'Client' object has no attribute 'prop'
# in order to set props on an object we need a constructor in the class

class Client:#this overwrites previous class declaration
    # constructor: specifies HOW to make the INITial object
    # instantiation: to make an instance of the class (an object)
    # objects, lists, sets(?), and dictionaries are the only MUTABLE data structures in Python
    def __init__(self):#the self param refers to the current object under construction
        self.name = "Client name"
        self.email = "Client email"
        self.dependents = []
    pass

client = Client()#
print(client)#
print(client.name)
print(client.email)
print(client.dependents)
# setter code for attribites declared on client object
client.name = "Elon"
client.email = "Elon@mars.com"
client.dependents.append("Grimes")
print(client.name)
print(client.email)
print(client.dependents)

# what if we wanted to assign to our fields at construction time?

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.dependents = []
    pass

# now we may call class with constructor args
# client = Client()
# TypeError: Client.__init__() missing 2 required positional arguments: 'name' and 'email'
client = Client("DW", "potus@gov.org")

# class methods (functions in a class)

class Client:
    def __init__(self, name, email):#overridden method (underscores)
        self.name = name
        self.email = email
        self.dependents = []
    def add_dependents(self, name):#custom method (no underscores)
        if name not in self.dependents:
            self.dependents.append(name)
    def __str__(self):
        return f"{self.name}, {self.email}, {self.dependents}"
    pass
#end class
client = Client("Elon", "em@mars.com")
client.add_dependents("Grimes")
client.add_dependents("AEX11")
print(client.name)
print(client.email)
print(client.dependents)
print(client)#Elon, em@mars.com, ['Grimes', 'AEX11']

# with the __str__ method supplied with its own custom implementation in our class
# it performs in this way
# print() looks for an implementation of __str__
# so the equivalent call to print could be
print(client.__str__())
# but call to __str__ is redundant

