# This routine illustrates Python classes and inheritance.

# 'Animal' is the parent class
class Animal:

    def __init__( self, name, age, purpose, legs=0 ):
        self.name    = name
        self.age     = age
        self.purpose = purpose
        self.legs    = legs          

    def report( self, a_type ):
        print( f"{self.name} is a {a_type}." )
        print( f"{self.name} is {self.age} years old, has {self.legs} legs, and is for {self.purpose}." )
        return
    
    def speak( self, sound ):
        print( f"{self.name} says {sound}." )
        print( " " )
        return


# Define the various child classes.
class Horse( Animal ):

    def speak( self, sound = 'Nay' ):
        super().speak( sound )                  # Call the 'speak' method of the parent class.
        return
    
    def report( self, a_type = 'Horse' ):
        super().report(a_type)                  # Call the 'report' method of the parent class.


class Cow( Animal ):

    def speak( self, sound = 'Moo' ):
        super().speak( sound )                  # Call the 'speak' method of the parent class.
        return
    
    def report( self, a_type = 'Cow' ):
        super().report(a_type)                  # Call the 'report' method of the parent class.

class Chicken( Animal ):

    def speak( self, sound = 'Ach buk buk' ):
        super().speak( sound )                  # Call the 'speak' method of the parent class.
        return
    
    def report( self, a_type = 'Chicken' ):
        super().report(a_type)                  # Call the 'report' method of the parent class.



# Main program, create some farm animals ard report them.
horse1 = Horse( 'Max', 4, 'transportation', 4 )
horse1.report()
horse1.speak()

cow1 = Cow( 'Sally', 2, 'food', 4 )
cow1.report()
cow1.speak()

chick1 = Chicken( 'Dodo', 3, 'food & eggs', 2 )
chick1.report()
chick1.speak()

# Display a few more 'internal' details.
print( "'horse1' is: ", type(horse1) )
print( horse1 )


# Display details on the 'objects'.
print( "For the 'horse1' object ... " )
for property, value in vars(horse1).items():
    print( property, " : ", value )



