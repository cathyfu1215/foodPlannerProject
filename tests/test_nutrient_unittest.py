'''
Cong (Cathy)Fu
Project - Food Planner
This is the unittest of the Nutrient class file .
'''

from unittest import TestCase
from models.nutrient import Nutrient


class NutrientTest(TestCase):

    def test_nutrient_init(self):
        new_nutrient = Nutrient(123, "Fe", 10.8)
        self.assertEqual(new_nutrient.nutrient_id, 123)
        self.assertEqual(new_nutrient.nutrient_web_name, "Fe")
        self.assertEqual(new_nutrient.nutrient_value, 10.8)
        self.assertEqual(new_nutrient.unit, "")

    def test_nutrient_init_wrong_nutrient_id_type(self):
        with self.assertRaises(TypeError):
            Nutrient("5", "Fe", 10.8)

    def test_nutrient_init_wrong_nutrient_web_name_type(self):
        with self.assertRaises(TypeError):
            Nutrient(5, None, 10.8)

    def test_nutrient_init_empty_nutrient_web_name_string(self):
        with self.assertRaises(ValueError):
            Nutrient(5, "", 10.8)

    def test_nutrient_init_wrong_nutrient_value_type(self):
        with self.assertRaises(TypeError):
            Nutrient(123, "Fe", "10.8")

    def test_nutrient_init_negative_nutrient_value_value(self):
        with self.assertRaises(ValueError):
            Nutrient(123, "Fe", -10.8)

    def test_nutrient_str(self):
        new_nutrient = Nutrient(123, "Fe", 10.8)
        self.assertEqual(str(new_nutrient), 'nutrient_id: 123, \
nutrient_web_name: Fe, \
nutrient_value: 10.8, unit: ')

    def test_nutrient_eq(self):
        new_nutrient = Nutrient(123, "Fe", 5.5)
        new_nutrient2 = Nutrient(456, "Cu", 6.6)
        new_nutrient3 = Nutrient(123, "Zn", 7.7)
        self.assertTrue(new_nutrient == new_nutrient3)
        self.assertFalse(new_nutrient == new_nutrient2)

    def test_nutrient_set_unit(self):
        new_nutrient = Nutrient(123, "Fe", 5.5)
        new_nutrient.set_unit("g")
        self.assertEqual(new_nutrient.unit, "g")

    def test_nutrient_set_empty_unit(self):
        with self.assertRaises(ValueError):
            new_nutrient = Nutrient(123, "Fe", 5.5)
            new_nutrient.set_unit("")

    def test_nutrient_get_id(self):
        new_nutrient = Nutrient(123, "Fe", 5.5)
        self.assertEqual(new_nutrient.get_id(), 123)

    def test_nutrient_get_name(self):
        new_nutrient = Nutrient(123, "Fe", 5.5)
        self.assertEqual(new_nutrient.get_name(), "Fe")

    def test_nutrient_get_value(self):
        new_nutrient = Nutrient(123, "Fe", 5.5)
        self.assertEqual(new_nutrient.get_value(), 5.5)

    def test_nutrient_get_unit(self):
        new_nutrient = Nutrient(123, "Fe", 5.5)
        new_nutrient.set_unit("g")
        self.assertEqual(new_nutrient.get_unit(), "g")

    def test_nutrient_value_is_zero_with_zero(self):
        new_nutrient = Nutrient(123, "Fe", 0.0)
        new_nutrient.set_unit("g")
        self.assertTrue(new_nutrient.nutrient_value_is_zero())

    def test_nutrient_value_is_zero_with_positive_value(self):
        new_nutrient = Nutrient(123, "Fe", 5.0)
        new_nutrient.set_unit("g")
        self.assertFalse(new_nutrient.nutrient_value_is_zero())
