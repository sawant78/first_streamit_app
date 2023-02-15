
import streamlit
import pandas
streamlit.title('My parents, new healthy dinner')

streamlit.header('Breakfats menu')
streamlit.text('Omega 3 and Blueberry oatmeal')
streamlit.text('Kale , spinach')
streamlit.text('Boiled Egg')

streamlit.header('Build your own fruit smoothie')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


