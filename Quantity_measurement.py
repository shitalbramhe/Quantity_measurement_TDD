"""
@Author: Shital Bajait
@Date: 18-02-2022 14:32:00
@Last Modified by: Shital Bajait 
@Last Modified time: 18-32-2022 14:32:00
@Title : compare lengths 1ft = 12in
"""
from InvalidTypeException import InvalidTypeException
from InvalidTypeException import ExceptionType
import logging

logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s: %(message)s')

file_handler = logging.StreamHandler()
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
 
class Quantitymeasurement(): 
    def feet_to_inch_Null(value):
        """
            Description:
                Function to check value is None
            Parameter:
                value
            Return:
                None
        """
        if not value is None:
            raise InvalidTypeException(ExceptionType.NONE_VALUE_EXCEPTION.value)
        logger.error('value is None')
        return None
    def feet_to_inch_value(value):
        """
            Description:
                Function to check value is greater than or equal to zero
            Parameter:
                value
            Return:
                value
        """
        if not value >= 0:
            raise InvalidTypeException(ExceptionType.VALUE_EXCEPTION.value)
        return value    
               
    def feet_to_inch_type(value):
        """
                Description:
                    Function to check data type of value
                Parameter:
                    value
                Return:
                    datatype
        """
        if not (isinstance(value, int)):
            raise InvalidTypeException(ExceptionType.TYPE_CHECK_EXCEPTION.value)
        return type(value)
                     
    def feet_to_inch_Reference(value):
        """
                Description:
                    Function to check reference of value
                Parameter:
                    value
                Return:
                    datatype
        """
        id(value) 
        return id(value)  

    def inch_to_feet(value, unit):
        """
                Description:
                    Function to convert inch to feet if unit is Feet
                Parameter:
                    value
                Return:
                    value in inch
        """
        if not unit == 'Inch':
           raise InvalidTypeException(ExceptionType.NOT_INCH_EXCEPTION.value)
        return value/12 
    
    def feet_to_inch(value, unit):
        """
                Description:
                    Function to convert feet to inch if unit is Feet
                Parameter:
                    value
                Return:
                    value in Feet
        """
        if not unit == 'Feet':
            raise InvalidTypeException(ExceptionType.NOT_FEET_EXCEPTION.value)
        return value*12
                
             
#if __name__ == '__main__':
 #   Quantitymeasurement.feet_to_inch_Null(8)
  #  Quantitymeasurement.feet_to_inch_value(-1)
   # Quantitymeasurement.feet_to_inch_type(8.9)
   

    
   