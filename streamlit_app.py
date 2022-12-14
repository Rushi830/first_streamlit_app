
import streamlit
import requests
import pandas
from urllib.error import URLError
streamlit.title('app testing check')
streamlit.header('Breakfast Menu')
streamlit.text('Bread')
streamlit.text('Butter')
streamlit.text('Jam')
streamlit.text('Milk')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 

# Let's put a pick list here so they can pick the fruit they want to include
my_fruit_list = my_fruit_list.set_index('Fruit')
#display the table on the page
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit. dataframe (fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice. com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    #streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
#streamlit.text(fruityvice_response.json())





#add_my_fruit = streamlit.text_input('What second fruit would you like information about?')
#streamlit.write('The user entered ', add_my_fruit)
#streamlit.write('Thanks for adding my fruit ', add_my_fruit)
