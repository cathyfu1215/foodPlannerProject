'''
Cong (Cathy)Fu
Project - Food Planner
This is the siderbar view file.
It contains three display functions.
'''


import streamlit as st


def get_user_input() -> str:
    '''
    This function checks the language selected, render the question
    to the user and return the user's input as a string
    '''
    if st.session_state['language'] == 'fr':
        st.header("Rechercher un aliment par son nom")
        user_input_food = st.text_input("Que veut-tu manger aujourd'hui?")
    else:
        st.header("Search food by its name")
        user_input_food = st.text_input("What do you want to eat today?")

    return user_input_food


def drop_down_menu(user_input_food: str) -> str or None:
    '''
    This function takes user's input food and
    the matched food list(from the session state),
    produce a drop down menu to the user so they can pick from that
    '''
    if st.session_state['food_list'] != []:
        if st.session_state['language'] == 'fr':
            st.write(f'{user_input_food}, bon choix')
            st.header("Pourriez-vous s'il vous plaît choisir une \
                        option dans le menu déroulant ?")
        else:
            st.write(f'{user_input_food}, good choice')

            st.header("Could you please pick one option from the \
                    drop down menu?")

        # the select box
        if st.session_state['language'] == 'fr':
            food_selection = st.selectbox(f'{user_input_food} \
                                        en détail...',
                                          st.session_state['food_list'],
                                          format_func=lambda x:
                                          x['food_description'],
                                          key="food_fr"
                                          )
        else:
            food_selection = st.selectbox(f'{user_input_food} in detail...',
                                          st.session_state['food_list'],
                                          format_func=lambda x:
                                          x['food_description'],
                                          key="food_en"
                                          )
        return food_selection

    # if we cannot find any matched food list, display the error message
    else:
        if st.session_state['language'] == 'fr':
            st.write('Oups, je ne trouve pas cette nourriture!😭')
        else:
            st.write('Oops, I cannot find this food!😭')


def display_food_full_name() -> None:
    '''
    This is a simple function that echos user's choice
    '''
    if 'food' in st.session_state:
        if st.session_state['language'] == 'fr':
            st.write("La nourriture que vous avez choisie est: ")
            st.write(f"{st.session_state['food'].get_food_description()}")

        else:

            st.write("The food you picked is: ")
            st.write(f"{st.session_state['food'].get_food_description()}")
