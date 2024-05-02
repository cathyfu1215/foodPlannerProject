'''
Cong (Cathy)Fu
Project - Food Planner
This is the Nutrient class file .
'''


class Nutrient:
    '''
    Represents a Nutrient with attributes and actions

    Attributes:
            nutrient_id: the identifier of the nutrient

            nutrient_web_name : the name of the nutrient

            nutrient_value: nutrient amount in 100g of the given food

            unit: a string, the unit of the nutrient value


    Methods:
        set_unit: modify the unit information attribute

        get_id: return the nutrient_id attribute

        get_name: return the nutrient_web_name attribute

        get_value: return the nutrient_value attribute

        get_unit: return the unit attribute

    '''

    def __init__(self, nutrient_id: int, nutrient_web_name: str,
                 nutrient_value: float):
        '''
        Initializes a new Food object with given attributes.

        Args:
            nutrient_id: the identifier of the nutrient
            nutrient_web_name : the name of the nutrient
            nutrient_value: nutrient amount in 100g of the given food

        Raises:
            TypeError: if nutrient_id is not an integer
                       if nutrient_web_name is not a string
                       if nutrient_value is not a float

            ValueError: if nutrient_value is less than zero
        '''
        if not isinstance(nutrient_id, int):
            raise TypeError('nutrient_id must be an integer')
        if not isinstance(nutrient_web_name, str):
            raise TypeError('nutrient_web_name must be a string')
        if not isinstance(nutrient_value, float):
            raise TypeError('nutrient_value must be an float')
        if len(nutrient_web_name) == 0:
            raise ValueError('nutrient_web_name must have a postive length')
        if nutrient_value < 0:
            raise ValueError('nutrient value must be a postive value or a 0')

        self.nutrient_id = nutrient_id
        self.nutrient_web_name = nutrient_web_name
        self.nutrient_value = nutrient_value

        # this attribute will be fetched from another URL, then combined here
        self.unit = ""

    def __str__(self) -> str:
        '''
        creates a string representation of the Nutrient

        Args:
            Nothing
        Returns:
           A string
        Raises:
            Nothing

        '''
        return f'nutrient_id: {self.nutrient_id}, \
nutrient_web_name: {self.nutrient_web_name}, \
nutrient_value: {self.nutrient_value}, unit: {self.unit}'

    def __eq__(self, other) -> bool:
        '''
        decides whether another object has the same type and nutrient_id
                with the current Nutrient
        Args:
            other: another object

        Returns a boolean

        Raises:
            Nothing
        '''
        if isinstance(other, Nutrient):
            if self.nutrient_id == other.nutrient_id:
                return True
        return False

    def set_unit(self, right_unit: str) -> None:
        '''
        modify the unit information attribute
        Raises:
            TypeError if the right_unit argument is not a string
            ValueError if the right_unit argument is empty
        '''
        if not isinstance(right_unit, str):
            raise TypeError('right_unit must be a string')
        if len(right_unit) == 0:
            raise ValueError('unit info must has a postive length')

        self.unit = right_unit

    def get_id(self) -> int:
        '''
        return the nutrient_id attribute
        '''
        return self.nutrient_id

    def get_name(self) -> str:
        '''
        return the nutrient_web_name attribute
        '''
        return self.nutrient_web_name

    def get_value(self) -> int:
        '''
        return the nutrient_value attribute
        '''
        return self.nutrient_value

    def get_unit(self) -> str:
        '''
        return the unit information attribute
        '''
        return self.unit

    def nutrient_value_is_zero(self) -> bool:
        '''
        This is a simple function that I will use
        in the future. The user can choose to filter
        out all the zero items in the nutrient detail
        display.
        '''
        return self.nutrient_value == 0
