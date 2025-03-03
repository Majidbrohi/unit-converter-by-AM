import streamlit as st

def unit_selector(unit_type):
    if unit_type == "Length":
        units = ["meters", "kilometers", "feet", "miles", "inches"]
    elif unit_type == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    elif unit_type == "Weight":
        units = ["grams", "kilograms", "pounds", "ounces"]
    elif unit_type == "Volume":
        units = ["liters", "milliliters", "gallons", "cubic meters"]
    else:
        units = []

    from_unit = st.sidebar.selectbox("From", units)
    to_unit = st.sidebar.selectbox("To", units)
    return from_unit, to_unit