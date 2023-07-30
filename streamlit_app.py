import streamlit
streamlit.title('My Parents New Healthy Diner');
streamlit.header('Breakfast Menu');
streamlit.text('🥣 Omega 3 and buleberry oatsmeal');
streamlit.text('🥗 Kale, spinach and Rocket smoothie');
streamlit.text('🐔 Hard-boiled and free-range egg');
streamlit.text('🥑🍞 Avocodo toast');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list1 = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list1.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list1.loc[streamlit.multiselect("Pick some fruits:", list(my_fruit_list1.index),['Avocado','Strawberries'])]

# Display the table on the page.
streamlit.dataframe(fruits_to_show);
