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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list);
