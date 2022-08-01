import streamlit
import pandas
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
my_fruit_list = my_fruit_list.set_index('Fruit')
#display the table on the page
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit. dataframe (my_fruit_list)
