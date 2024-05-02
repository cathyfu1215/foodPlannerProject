'''
Cong (Cathy)Fu
Project - Food Planner
This is the main display view file.
'''

import streamlit as st
import pandas as pd


def title_display() -> None:
    '''
    Displays the title of the App in the right language
    '''
    if 'language' in st.session_state:
        if st.session_state['language'] == 'fr':
            st.title("Nutriments dans les aliments🍎")
            st.subheader("Planifiez vos repas quotidiens \
et mangez sainement!")
        else:
            st.title("Nutrients in Food🍎")
            st.subheader("Plan your daily meals and eat healthily!")
    else:
        st.write('Please select language and food from the sidebar')
        st.write("Veuillez sélectionner la langue et la \
nourriture dans la barre latérale")

    st.divider()


def content_display() -> None:
    '''
    Displays the nutrient content of the Food in the right language
    '''
    if 'food' in st.session_state:
        st.write(f"In 100g \
{st.session_state['food'].get_food_description()}, it contains: ")

        nutrient_array = []
        for item in st.session_state['food'].get_food_nutrients():
            nutrient_array.append([item.get_name(), item.get_value(),
                                  item.get_unit()])

        result = pd.DataFrame(nutrient_array,
                              columns=['Nutrient Name', 'Nutrient Value',
                                       'Unit'])

        st.dataframe(result, hide_index=True, use_container_width=True)
    else:
        if st.session_state['language'] == 'fr':
            st.write('Après sélection, je vais le chercher pour vous...')
        else:
            st.write('After selection, I will fetch it for you...')


def main_display() -> None:
    '''
    The main view of chosen food

    It contains:
        1.The title of the App
        2.Display of detail of nutrients in selected food
    '''
    title_display()
    content_display()
