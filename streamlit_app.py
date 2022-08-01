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
streamlit.dataframe(my_fruit_list)
