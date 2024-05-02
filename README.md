# food_planner_project

## Project Summary
I care about eating healthily and I hope my project can help people like me. This is a simple project that takes the user's choice of food and displays reliable nutrient values of the food. The data I used is from Open Data, Government Canada. This project supports food searching and nutrient information displaying in both English and French.

## Description of the REST API(s)
* REST API: Canadian Nutrient (CNF) API
* URL: https://food-nutrition.canada.ca/api/canadian-nutrient-file
* Documentation: https://produits-sante.canada.ca/api/documentation/cnf-
documentation-en.html
* Endpoints:
  * `/food/?lang=fr`
    - get a list of foods in French
  * `/food`
    - get a list of foods in English
  * `/nutrientname/?lang=fr`
    - get a list of nutrients in French 
  * `/nutrientname`
    - get a list of nutrients in English
  * `/nutrientamount/?lang=fr&id=food_code`
    - get a list of nutrient amount info for specific food, in French
  * `/nutrientamount/?id=food_code`
    - get a list of nutrient amount info for specific food, in English
   
## Description of the process:
* Invite the user to pick their preferred language
* Fetch the food data in that language and create Food objects
* Invite user to enter their food choice
* After user entered their food choice, match the input from the previously fetched
food data and create a drop-down menu displaying all specific food options
* After the user picks a specific food from the drop-down menu, fetch the specific
food nutrient amount details
* Fetch unit information from fetching the list of nutrient data
* Combine the unit information and the specific nutrient amount details, create a list
of Nutrient objects
* Display the nutrient objects

## Features & Interactions

### Feature #1 : language selection
* The users can first choose their preferred language (English or French) and see different displays of the main page and the sidebar.
* Switching between languages will load all contents again.
* No classes are used here.
* This feature is in my “sidebar view”.

### Feature #2 : text input and search
* The users can enter their desired food name into an input box.
* When they hit enter, the app will search all the matched food (in detail, for
example, how the food is cooked , or what brand if this food) from the database, and create a drop-down menu for them so they can pick the item that matches their desired food the most.
* Class Food is used in this feature.
* This feature is in the “sidebar view”.

### Feature #3: choose from drop down menu and display
* Users can choose the specific food item from the drop-down menu and my app will render the detailed nutrient facts about this food.
* The display is rendered by a pandas data frame.
* Users can sort the data, or search for a specific nutrient name.
* Class Nutrient is used in this feature.
* This feature is in the “sidebar view”.


## Data Classes
(Please refer to my doctoring of the classes : Food and Nutrient) 
#### Food objects contain three attributes:
* food_code (integer, a unique identifier)
* food_description (string, the name of the food, also the display on the dropdown
menu)
* nutrient (a list of Nutrient objects the food contains)
  
#### Nutrient objects contain four attribute:
* nutrient_id (integer, a unique identifier)
* nutrient_web_name (string, the name of the nutrient )
* nutrient_value (float, the amount of nutrient value in 100g of the selected food)
* nutrient_unit(string, the unit of the nutrient value)

These items are fetched from two sets of fetched data.
From the nutrient list, we fetch the nutrient_id and the unit information (for example, “g”, or “mg”) for a nutrient.
From the nutrient amount info of a specific food, we fetch the food_code of the food where the nutrient is in, nutrient_id , and the name of the nutrient, and the amount of this nutrient in 100 grams of the specific food (nutrient_value).
With the two sets of information, I join them by using the shared unique key (nutrient_id) and create the Nutrient objects.

## Data structures
* Lists : I put my created Food objects and Nutrient objects into lists so they can be searched and displayed (I used several iterations).
* At the same time I used the session state of the streamlit library. It feels like a global Dictionary so I can load the language selection of my users and the corresponding food and nutrient results into the session state. When users change their language selections, those “values” in the key-value pairs of the session state will change, and my content can also change.

## Functions for fetching and cleaning data
I have three functions for fetching data. 

#### 1.get_food_data() function
* This function returns a list of food options from the API.
* The function does not take any parameters.
* Inside the list, there are multiple dictionaries consisting of food_code (int) and
food_descriptions (str). These dictionaries will be used to create Food objects later.

#### 2.get_nutrient_data() function
* This function returns a list of nutrients from the API.
* The function does not take any parameters.
* Inside the list, there are multiple dictionaries consisting of nutrient_name_id(int),
nutrient_name(str), unit(str), and so on.

#### 3.get_nutrient_amount(food_code) function
* This function gets a list of nutrients of a specific food, from the API.
* It takes a parameter, which is the unique identifier of the food: food_code (an integer).

I do not have functions for cleaning data, since my data is from Government Canada and they are “fixed” data (they are the nutrient values of a specified food, so they do not change). They are nicely documented and maintained.Currently I don’t see any need for cleaning them.


## Views
I will have two views: the sidebar and the main display.
* In the sidebar, it contains all the interactions with the user. Users can choose their preferred language, enter the food they want to pick, and select the specific food name from my drop-down menu.
* In the main display view, it only renders the result of the user's input. Users can sort the rendered result.

## Environmental Setup
1. Clone the project repository / Download the zip file of the project
2. Navigate to the project directory
   ```cd foodPlannerProject```
3. Install the dependencies using pip
   ```pip  install -r requirements.txt``` or ```pip3 install -r requirements.txt```
4. Run the app.py script
   ```streamlit run app.py``` or   ```python3 -m streamlit run app.py```

## Code Highlights
I am proud of finding a reliable API, reading the documentation carefully and designing how I joined my three data sets using their shared unique keys.

### a. Food Data , which has a structure like this
```
[
  {
    "food_description": "Chicken, broiler, giblets, raw"
  }
]
```

### b. Nutrient Data , which has a structure like this
```
[
  {
  "nutrient_name_id": 550,  # the unique key
  "nutrient_symbol": "ASPA",
  "nutrient_name": "ASPARTAME",
  "unit": "mg",  # the info I need
  "nutrient_code": 550,
  "tagname": "",
  "nutrient_decimals": 0,
  "nutrient_web_order": 15,
  "nutrient_web_name": "Aspartame",
  "nutrient_group_id": 7
  }
]
```


