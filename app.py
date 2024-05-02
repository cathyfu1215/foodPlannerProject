'''
Cong (Cathy)Fu
Project - Food Planner
This is the main file /main page of my project.
'''

from requests.exceptions import HTTPError, ConnectionError
from models.food import Food
import streamlit as st
import views.sidebar
import views.main_display
import utils.fetch_data_functions as fetch_data_functions
import utils.process_data as process_data


def language_select() -> None:
    '''
    Displays language selection buttons (EN and FR).
    After user's clicking, the language setting will change to
    the selected language, the program will fetch the
    data in that language and display them.
    '''
    st.header("Please choose language")
    st.header("Veuillez choisir la langue")
    en_button = st.button("EN 🇬🇧", key="en_button")
    if en_button:
        st.session_state['language'] = "en"

    fr_button = st.button("FR 🇫🇷", key="fr_button")
    if fr_button:
        st.session_state['language'] = "fr"


def sidebar_commands() -> None:
    '''
    This part handles all the user input (after language selection)

    0. User input food name in the text box
    1. Validate the input
    2. Fetch all the food names matching the user's input
    3. Display the matched food names in a drop down menu
    4. User choose from the drop down menu again
    '''

    # If language is not selected, this part will simply not show up
    # so user can focus on selecting the language

    if 'language' in st.session_state:
        user_input_food = views.sidebar.get_user_input()

        # user input validation
        # This is the only necessary validation
        # If there is no input (length == 0 ),
        # I will just wait for input
        if len(user_input_food) > 0:

            # store all the food that match user input in session state
            st.session_state['food_list'] = \
                process_data.get_food_list(user_input_food)

            # create a drop down menu in the views
            food_selection =\
                views.sidebar.drop_down_menu(user_input_food)

            # if user selects one of the options,
            # create a food object that will take nutrient
            # info later in the process
            if food_selection:
                st.session_state['food'] =\
                    Food(food_selection['food_code'],
                         food_selection['food_description'])

            views.sidebar.display_food_full_name()


def display_nutrient_data() -> None:
    '''
    This part is in charge of fetching the nutrient amount
    information, fetch all nutrient units information , create
    nutrient objects and put them in the food object's nutrient list.

    After all the processing, it will display the nutrient information
    '''
    # if language or food is not selected yet, we won't fetch anything
    if 'language' in st.session_state:
        if 'food' in st.session_state:

            # fetch the nutrient amount info for specific food
            food_nutrient_amount =\
                fetch_data_functions.get_nutrient_amount(
                    st.session_state['food'].get_food_code())

            # prepare a list of Nutrient objects to put in the
            # food object
            nutrient_list = process_data.get_nutrient_list(
                food_nutrient_amount)

            # put Nutritent objects into the food object
            st.session_state['food'].set_nutrients(nutrient_list)

        # Display the main nutrient information
        views.main_display.main_display()


def main():
    '''
    The main function/main page
    It contains three parts:
        0.the sidebar -- language selection
        1.the sidebar -- user can make selections and enter info here
        2.the main display -- detail of selected food
    '''

    try:
        with st.sidebar:
            language_select()
            sidebar_commands()
        display_nutrient_data()

    except TypeError as ex:
        print(type(ex), ex)
    except ValueError as ex:
        print(type(ex), ex)
    except ConnectionError as ex:
        print(type(ex), ex)
    except HTTPError as ex:
        print(type(ex), ex)


if __name__ == "__main__":
    main()
