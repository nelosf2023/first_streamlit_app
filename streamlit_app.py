import streamlit
import pandas
# import request library
import requests
import snowflake.connector

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

#change index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

# truncate dataframe to selected fruits
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# add fruity api header
streamlit.header("Fruityvice Fruit Advice!")

# add user fruit input for api call
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


# add fruity api request
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# change fruity api response from json to dataframe
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

# connect to snowflake and query
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# create variable that recieves the fruit the user would like to add
add_my_fruit = streamlit.text_input("What fruit would you like to add?",'aaa')
streamlit.write('Thank you for adding ', add_my_fruit)
