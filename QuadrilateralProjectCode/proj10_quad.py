
import math

################################################################################
## Class Quad
################################################################################

class Quad( object ):
    def __init__( self, AB=None, DA=None, A=90 ):
        """
        Initialize an object of type Quad.
        """
        
        self.__sideAB = float(AB)
        if DA == "None":
            DA = AB
        self.__sideDA = float(DA)
        self.__angleA = float(A)
        self.__valid = False
        
        
        
    def __validate( self ):
        #
        # Determine if a Quad is valid.
        #
        
        if self.__sideAB > 0 and self.__sideDA > 0 and self.__angleA >0 and self.__angleA <360:
            self.__valid =True
        else:
            self.__valid =False
        return self.__valid
    
    def __repr__( self ):
        """
        Return a string (the representation of a Quad).
        """
        side1="{:.1f}".format(self.__sideAB)
        side2="{:.1f}".format(self.__sideDA)
        sides_list=[side1, side2, side1, side2]
        return  sides_list

    def __str__( self ):
        """
        Return a string (the representation of a Quad).
        """
        return "str method called"


    def is_valid( self ):
        """
        Return a Boolean (is the Quad valid?).
    
        """
        if self.__validate():
            return True
        else:
            return False
        
    def is_rectangle( self ):
        """
        Return a Boolean (is the Quad a rectangle?)
        """
        if self.__sideAB != self.__sideDA and self.__angleA ==90:
            return True
        else:
            return False
        
    def is_rhombus( self ):
        """
        Return a Boolean (is the Quad a rhombus?)
        """
    
        pass # REPLACE

    def is_square( self ):
        """
        Return a Boolean (is the Quad a square)?
        """
        if self.__sideAB == self.__sideDA and self.__angleA ==90:
            return True
        
        else:
            return False
    def sides( self ):
        """
        Return a tuple containing the Quad's four sides.
        """
        sides_tuple=(self.__sideAB,self.__sideDA,self.__sideAB,self.__sideDA)
        return sides_tuple
        
    def angles( self ):
        """
        Return a tuple containing the Quad's four angles (in degrees)
        #if valid parallelogram else return (None,None,None,None)
        """
        if self.is_valid():
        
           angle_tuple=(self.__angleA,180-self.__angleA,self.__angleA,180-self.__angleA)
        else:
            return (None,None,None,None)
        
        
    def perimeter( self ):
        """
        Return a float representing the Quad's perimeter.
        return perimeter when valid else zero
        """
        if self.is_valid():
            return (2*(self.__sideAB + self.__sideDA))
        else:
            return 0
    
    def area( self ):
        """
        Return a float representing the Quad's area.
        """
        if self.is_valid():
            return (self.__sideAB*self.__sideDA)
        else:
            return 0

    def scale( self, factor=1.0 ):
        """
        Scale all four of a Quad's sides by the same factor.
        #*factor (>0)
        """
        if self.is_valid() and factor >0:
            self.__sideAB=factor*self.__sideAB
            self.__sideDA=factor*self.__sideDA
            
            

