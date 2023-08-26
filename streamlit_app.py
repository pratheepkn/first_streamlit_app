import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.title('My Momo\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Lets put a pick list here so they can pick the fruit thwy want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


#/* #New section to display fruityvice api response
#streamlit.header('Fruityvice Fruit Advice!')
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# json version and normalize it

#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# format as table
#streamlit.dataframe(fruityvice_normalized)
#*/

#/*
#streamlit.header('Fruityvice Fruit Advice!')
#try:
 # fruit_choice = streamlit.text_input('What fruit would like to information about?')
  #if not fruit_choice:
   # streamlit.error("Please select a fruit to get information.")
  #else:
   # fruityvise_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    #streamlit.dataframe(fruityvice_normalized)
#except URLError as e:
 # streamlit.error()
#*/
#create the repeatable code block called function
def get_fruityvice_data(this_fruit_choice):
    fruityvise_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
#New section to display fruityvice api response
streamlit.header('Fruityvice fruit advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would like to information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
 

#Connect with snowflake
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
#my_data_rows = my_cur.fetchall()
#streamlit.stop()
#streamlit.text("Hello from Snowflake:")
#streamlit.text("The fruit load list contains")
#streamlit.text(my_data_row)
#streamlit.header("The fruit load list contains")
#streamlit.dataframe(my_data_rows)

streamlit.header("The fruit load list contains")
#snowflake related functions
def get_fruit_load_list():
  with my.cnx.cursor() as my_cur:
       my.cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()
#Add a button to load the fruit
if streamlit.button('Get Fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

#Allow the end user to add a fruit to list
#add_my_fruit = streamlit.text_input('What fruit would you like add?')
#streamlit.write('Thanks for adding ', add_my_fruit)
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

dev insert_row_snowflake(new_fruit):
 with my_cnx.cursor() as my_cur:
   my_cur.execute("insert into fruit_load_list values ('from streamlit')")
   return "Thanks for adding" + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like add?')

if streamlit.button('Add a Fruit to the list')
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)

#Allow the end user to add a fruit to list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values ('" + new_fruit +"')")
       return "Thanks for adding " + new_fruit


