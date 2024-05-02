'''
Cong (Cathy)Fu
Project - Food Planner
This is the Food class file .
'''

import re


class Food:
    '''
    Represents a Food with attributes and actions relevant to
    its nutrient values

    Attributes:
        food_code : an integer that is the unique key of the food
                    item in the database
        food_description: a string that is the specific cook method
                          of the given food
        nutrients: a list of nutirent objects that belongs to this specific
                   food

    Methods:
        set_nutrients: modify the food object's attribute

        get_food_code: return the food_code attribute

        get_food_description: return the food_description attribute

        get_food_nutrients:return the nutrient attribute


    '''
    def __init__(self, food_code: int, food_description: str):
        '''
        Initializes a new Food object with given attributes.

        Args:
            food_code: the identifier of the food
            food_description: the detail of the food
            nutrients: a list of nutirent objects this food contains


        Raises:
            TypeError: if food_code is not an integer
                       if food_description is not a string

            ValueError: if food_description is an empty string

        '''
        # the food code can be any integer, even a negative integer

        if not isinstance(food_code, int):
            raise TypeError('food_code must be an integer')
        if not isinstance(food_description, str):
            raise TypeError('food_description must be a string')
        if len(food_description) == 0:
            raise ValueError('food_description cannot be empty')

        self.food_code = food_code
        self.food_description = food_description

        # when we initialize the food, we don't need the nutrient info
        # we fetch the nutrient info when user selected this food
        self.nutrients = []

    def __str__(self) -> str:
        '''
        creates a string representation of the Food

        Args:
            Nothing
        Returns:
           A string
        Raises:
            Nothing

        '''
        return f'food_code: {self.food_code}, \
food_description: {self.food_description}, \
nutrients: {self.nutrients}'

    def __eq__(self, other) -> bool:
        '''
        decides whether another object has the same type, food
        code and description with the current Food
        Args:
            other: another object

        Returns a boolean

        Raises:
            Nothing
        '''
        if isinstance(other, Food):
            if self.food_code == other.food_code:
                if self.food_description == other.food_description:
                    return True
        return False

    def set_nutrients(self, nutrients: list) -> None:
        '''
        modify the food object's attribute
        Raises:
            TypeError if the given nutrients is not a list
            ValueError if the given list is empty
        '''
        if not isinstance(nutrients, list):
            raise TypeError('nutrients must be a list')
        if len(nutrients) == 0:
            raise ValueError('nutrients must not be an empty list')
        self.nutrients = nutrients

    def get_food_code(self) -> int:
        '''
        return the food_code attribute
        '''
        return self.food_code

    def get_food_description(self) -> str:
        '''
        return the food_description attribute
        '''
        return self.food_description

    def get_food_nutrients(self) -> list:
        '''
        return the nutrient attribute
        '''
        return self.nutrients

    def food_is_raw(self) -> bool:
        '''
        This is a simple method I will use in the future,
        to deterimine if the food has a "raw" string in its name
        (so we need to cook before consuming it).
        '''
        pattern = re.compile('raw', flags=re.IGNORECASE)
        food_is_raw = re.match(pattern, self.food_description) is not None
        return food_is_raw
