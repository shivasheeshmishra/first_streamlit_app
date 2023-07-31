import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner');
streamlit.header('Breakfast Menu');
streamlit.text('🥣 Omega 3 and buleberry oatsmeal');
streamlit.text('🥗 Kale, spinach and Rocket smoothie');
streamlit.text('🐔 Hard-boiled and free-range egg');
streamlit.text('🥑🍞 Avocodo toast');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list1 = my_fruit_list.set_index('Fruit');
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list1.index),['Avocado','Strawberries']);
fruits_to_show = my_fruit_list1.loc[fruits_selected];
# Display the table on the page.
streamlit.dataframe(fruits_to_show);
# Create a function
def get_fruityvice_data (this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice);
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json());
    return fruityvice_normalized;
streamlit.header("Fruityvice Fruit Advice!");
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?');
    if not fruit_choice:
      streamlit.error("Please select a fruit to get information");
#streamlit.write('The user entered ', fruit_choice);
#import requests
    else:
      back_from_function = get_fruityvice_data(fruit_choice);
      streamlit.dataframe(back_from_function);
except URLError as e:
  streamlit.error();
#import snowflake.connector
streamlit.header("View Our FRUIT LIST And Add Your Favorites :");
#Snowflake-related-function
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
         return my_cur.fetchall();
#Add a button to load fruit
if streamlit.button ('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]);
    my_data_rows = get_fruit_load_list();
    streamlit.dataframe(my_data_rows);
    my_cnx.close();
# Allow end user to add fruit to list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ("+streamlit.text(new_fruit)+")");
        return "Thanks for adding " +new_fruit;
add_my_fruit = streamlit.text_input('What fruit would you like to add?');
if streamlit.button ('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]);
    back_from_function = insert_row_snowflake(add_my_fruit);
    streamlit.text(back_from_function);
    my_cnx.close();
