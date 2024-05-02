'''
Cong (Cathy)Fu
Project - Food Planner
This is the unittest of the Food class file .
'''

from unittest import TestCase
from models.food import Food


class FoodTest(TestCase):
    '''
    Unit test for the Food class
    '''
    def test_food_init(self):
        new_food = Food(123, "Apple Pie")
        self.assertEqual(new_food.food_code, 123)
        self.assertEqual(new_food.food_description, "Apple Pie")
        self.assertEqual(new_food.nutrients, [])

    def test_food_init_wrong_food_code_type(self):
        with self.assertRaises(TypeError):
            Food("5", "Apple Pie")

    def test_food_init_wrong_food_description_type(self):
        with self.assertRaises(TypeError):
            Food(5, None)

    def test_food_init_empty_food_description_value(self):
        with self.assertRaises(ValueError):
            Food(5, "")

    def test_food_str(self):
        new_food = Food(123, "Apple Pie")
        self.assertEqual(str(new_food), 'food_code: 123, \
food_description: Apple Pie, nutrients: []')

    def test_food_eq(self):
        new_food = Food(123, "Apple Pie")
        new_food2 = Food(456, "Banana Pie")
        new_food3 = Food(123, "Apple Pie")
        self.assertTrue(new_food == new_food3)
        self.assertFalse(new_food == new_food2)

    def test_set_nutrients(self):
        new_food = Food(123, "Apple Pie")
        new_food.set_nutrients(['item1', 'item2'])
        self.assertEqual(new_food.nutrients, ['item1', 'item2'])

    def test_set_empty_list_to_nutrients(self):
        with self.assertRaises(ValueError):
            new_food = Food(123, "Apple Pie")
            new_food.set_nutrients([])

    def test_get_food_code(self):
        new_food = Food(123, "Apple Pie")
        self.assertEqual(new_food.get_food_code(), 123)

    def test_get_food_description(self):
        new_food = Food(123, "Apple Pie")
        self.assertEqual(new_food.get_food_description(), "Apple Pie")

    def test_get_food_nutrients(self):
        new_food = Food(123, "Apple Pie")
        new_food.set_nutrients(['item1', 'item2'])
        self.assertEqual(new_food.get_food_nutrients(), ['item1', 'item2'])

    def test_food_is_raw(self):
        new_food = Food(123, "raw Apple")
        self.assertTrue(new_food.food_is_raw())

    def test_food_is_raw_with_capital_letters(self):
        new_food = Food(123, "RAW Apple")
        self.assertTrue(new_food.food_is_raw())

    def test_food_is_raw_with_not_raw_food(self):
        new_food = Food(123, "Apple Pie")
        self.assertFalse(new_food.food_is_raw())
