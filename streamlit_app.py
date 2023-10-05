import streamlit
import pandas

streamlit.title('My Mom\'s New Healthy Diner')
# add header and text
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
# add another header
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import s3 bucket fruit data
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# show dataframe on page
streamlit.dataframe(my_fruit_list)
