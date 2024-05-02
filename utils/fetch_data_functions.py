'''
Cong (Cathy)Fu
Project - Food Planner
This is the function file that contains functions that
fetches data from API and functions that process user input.
'''
import requests
from requests.exceptions import HTTPError, ConnectionError
import streamlit as st

# This is the main API , everything comes from here
CANADIAN_NUTRIENT_FILE_API = 'https://food-nutrition.canada.ca/api/' +\
    'canadian-nutrient-file/'


def get_food_data() -> list:
    '''
    This function gets a list of food options from the API

    Inside the list, there are multiple dictionaries consisting
    food_code (int) and food_descriptions (str).

    These dictionaries will be used to create Food objects later.

    Since I put the language variable in session state, this
    function will automatically fetch the list in the right language

    Raises:
        HTTPError
        ConnectionError


    '''
    try:
        if st.session_state['language'] == "fr":
            response = requests.get(CANADIAN_NUTRIENT_FILE_API
                                    + "/food"+"/?lang=fr")
        else:
            response = requests.get(CANADIAN_NUTRIENT_FILE_API + "/food")
        response.raise_for_status()
        food = response.json()

        if food is None:
            raise ValueError("food data is lost!")
    except HTTPError as ex:
        raise (ex)
    except ConnectionError as ex:
        raise (ex)

    else:
        return food


def get_nutrient_data() -> list:

    '''
    This function gets a list of nutrients from the API

    Inside the list, there are multiple dictionaries consisting
    nutrient_name_id(int), nutrient_name(str), unit(str), and so on.

    These dictionaries will be used to create Nutrient objects later.

    Since I put the language variable in session state, this
    function will automatically fetch the list in the right language

    Raises:
        HTTPError
        ConnectionError
    '''

    try:
        if st.session_state['language'] == "fr":
            response = requests.get(CANADIAN_NUTRIENT_FILE_API
                                    + "/nutrientname" + "/?lang=fr")
        else:
            response = requests.get(CANADIAN_NUTRIENT_FILE_API
                                    + "/nutrientname")
        response.raise_for_status()
        nutrients = response.json()
        if nutrients is None:
            raise ValueError("nutrient data is lost!")
    except HTTPError as ex:
        raise (ex)
    except ConnectionError as ex:
        raise (ex)
    else:
        return nutrients


def get_nutrient_amount(food_code: int) -> list:
    '''
    This function gets a list of nutrients of a specific food,
    from the API.

    Inside the list, there are mutiple dictionaries representing each
    nutrient inside the given food. It contains the key food_code (int),
    which is used to join the food data and the nutrient data.

    These dictionaries will be used to create Nutrient objects later.

    Since I put the language variable in session state, this
    function will automatically fetch the list in the right language

    Raises:
        HTTPError
        ConnectionError
    '''
    try:
        if st.session_state['language'] == "fr":
            response = requests.get(CANADIAN_NUTRIENT_FILE_API +
                                    "/nutrientamount" + "/?lang=fr"
                                    + "&id=" + str(food_code))
        else:
            response = requests.get(CANADIAN_NUTRIENT_FILE_API +
                                    "/nutrientamount" + "/?id="
                                    + str(food_code))
        response.raise_for_status()
        nutrient_amount = response.json()
        if nutrient_amount is None:
            raise ValueError("nutrient amount data is lost!")
    except HTTPError as ex:
        raise (ex)
    except ConnectionError as ex:
        raise (ex)

    else:
        return nutrient_amount
