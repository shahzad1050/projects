import streamlit as st

def unit_converter(value : float ,unit_from : str , unit_to: str):

    if unit_from == "kilometers" and unit_to == "meters":
     return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
       return value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
       return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
     return value * 0.001
    else:
        "not supported"

def unit():
   st.title("UNIT CONVERTER")
   st.header("welcome to unit converter!")

   value= st.number_input("enter the number")
   unit_from = st.text_input("e.g. kilometers ,meters ,kilograms ,gram")
   unit_to = st.text_input("e.g. kilometes ,meters ,kilograms ,grams")

   if st.button("click here"):
      result = unit_converter(value, unit_from, unit_to)
      st.write("value converted", result)

unit()