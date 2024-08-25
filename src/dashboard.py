import streamlit as st
from src.password_generator import MemorablePasswordGenerator, RandomPasswordGenerator, PinCodeGenerator

st.image("https://iccup.com/upload/images/news/eunews/Password-main.png", width = 500)
st.title(":lock: Password Generator")

option = st.radio(
    "Select a password type",
    ("Random Password", "Memorable Password", "Pin Code")
)

if option == "Pin Code":
    length = st.slider("Select the length of your pin code", 4, 32)
    generator = PinCodeGenerator(length)

elif option == "Random Password":
    length = length = st.slider("Select the length of your random password", 4, 32)
    include_numbers = st.toggle("Do you want your passwword to include numbers?")
    include_symbols = st.toggle("Do you want your passwword to include symbols?")
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)

elif option == "Memorable Password":
    number_of_words = st.slider("Select the number of words in your password:", 4, 10)
    separator = st.text_input("Seperatpr: ", value='-')
    capitalize = st.toggle("Capitalization: ")
    generator = MemorablePasswordGenerator(number_of_words, separator, capitalize)

password = generator.generate()
st.write(fr"Your password is: ``` {password} ``` ")