
import streamlit
import pandas
streamlit.title('My parents, new healthy dinner')

streamlit.header('Breakfats menu')
streamlit.text('Omega 3 and Blueberry oatmeal')
streamlit.text('Kale , spinach')
streamlit.text('Boiled Egg')

streamlit.header('Build your own fruit smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


