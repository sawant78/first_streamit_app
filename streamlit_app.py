
import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError
streamlit.title('My parents, new healthy dinner')

streamlit.header('Breakfats menu')
streamlit.text('Omega 3 and Blueberry oatmeal')
streamlit.text('Kale , spinach')
streamlit.text('Boiled Egg')

streamlit.header('Build your own fruit smoothie')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output to the screen as a table
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur1 = my_cnx.cursor()
my_cur1.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row1 = my_cur1.fetchall()
streamlit.text("Fruitload list is:")
streamlit.dataframe(my_data_row1)

streamlit.header("Allow end user to add fruits!")
fruit_choice_add = streamlit.text_input('What fruit would you like add in the list about?')

my_cur1.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")






