import streamlit as st
import pandas as pandas
import datetime

st.header("Streamlit Application Web page")

st.title("Hello world!!")

st.write("Welcome to streamlit")

st.image("zoom2.jpg", caption="Image caption", use_column_width=True)


st.subheader("Buttons")

if st.button("Click me"):
    st.write("Button clicked!")


st.subheader("Sliders")    

slider_value = st.slider("Select a value:", min_value=0, max_value=100, value=50)

st.write(f"Selected value: {slider_value}")

checkbox_value = st.checkbox("Show content")
if checkbox_value:
    st.write("Content displayed.")

name = st.text_input("Enter your name:", "Type here")
st.write(f"Hello, {name}!")    


feedback = st.text_area("Your feedback:", "Type your feedback here")
st.write(f"Thank you for your feedback: {feedback}")


time = st.time_input("Select a time:", datetime.time(12, 00))
st.write(f"Selected time is: {time}")

options = ["Option 1", "Option 2", "Option 3"]
choice = st.selectbox("Choose an option:", options)
st.write(f"You chose: {choice}")