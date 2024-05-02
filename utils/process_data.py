'''
Cong (Cathy)Fu
Project - Food Planner
This is the function file that contains helper functions
for processing data.
'''

import re
from models.food import Food
import streamlit as st
from models.nutrient import Nutrient
import utils.fetch_data_functions as fetch_data_functions


def get_food_list(user_input_food: str) -> list:
    '''
    This function consumes user's choices of food and return
    a list of all the matches in the food data we have fetched from the API
    before

    Later, user can choose a specific food (and the cooking method) and
    get the details of the nutrients
    '''
    # fetch all the food name/description data from API
    st.session_state['all_food_list'] = fetch_data_functions.get_food_data()

    # match food names with user input
    match_food_list = []

    for item in st.session_state['all_food_list']:
        food_item = Food(item['food_code'], item['food_description'])
        pattern = re.compile(user_input_food, flags=re.IGNORECASE)
        if re.search(pattern, food_item.food_description) is not None:
            match_food_list.append(item)

    return match_food_list


def get_nutrient_list(food_nutient_amount: list) -> list:
    '''
    This function consumes a list of nutrients of a given food,
    create objects of the Nutrient class, put them into a list
    and return the list.
    '''
    nutrients_list = []
    for item in food_nutient_amount:

        nutrient_item = Nutrient(item['nutrient_name_id'],
                                 item['nutrient_web_name'],
                                 item['nutrient_value'])

        # match the right unit to the right nutrient
        nutrients = fetch_data_functions.get_nutrient_data()
        for nutri in nutrients:
            if nutri['nutrient_name_id'] == nutrient_item.get_id():
                nutrient_item.set_unit(nutri['unit'])

        nutrients_list.append(nutrient_item)

    return nutrients_list
