import streamlit as st
import pandas as pd

#Printing a line
st.write('Hello Pakistan! Learning Streamlit')
#creating a button
st.header('Button')
#declaring button and when press it say have a good day
if st.button('Press Me'):
    st.write('Have a good day dear!')
else:
    st.write('Good Bye!')

st.write("""
# Learning New Things

Let's get started
"""
)

st.write(1234)

st.write('Hello Misbah Aleem')

df=pd.DataFrame(
    {
   'Name':["Fatima", 'Misbah', 'Zahra'],
   'Age': [26, 25, 2]
}
)
st.write(df)
st.write("""
  # Display Bar Chart       
         
         
         """)

st.bar_chart(df)
st.caption(' ### Bar Chart Display')
