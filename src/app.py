import streamlit as st
import pandas as pd
from components import unit_selector, conversion_history
from utils import convert_units
import os

st.set_page_config(page_title="Unit Converter", layout='wide')
st.title(" 🔢 Unit Converter™️")

# Sidebar for unit selection
st.sidebar.header("Select Units")
unit_type = st.sidebar.selectbox("Choose a unit type", ["Length", "Temperature", "Weight", "Volume"])
from_unit, to_unit = unit_selector(unit_type)

# Input for the value to convert
value_input = st.text_input(f"Enter value in {from_unit}:", placeholder="Enter value")

# Convert the input to a float
try:
    value = float(value_input)
except ValueError:
    value = None

# Initialize result variable in session state
if 'result' not in st.session_state:
    st.session_state.result = None

# Convert the value
if st.button("Convert"):
    if value is None:
        st.error("Please enter a valid number.")
    elif from_unit == to_unit:
        st.warning("Please select different units for conversion.")
    else:
        st.session_state.result = convert_units(value, from_unit, to_unit)
        st.session_state.result = round(st.session_state.result, 2)
        st.success(f"{value:.2f} {from_unit} is equal to {st.session_state.result:.2f} {to_unit}")

        # Display the result attractively
        st.markdown(f"""
            <div style="border: 2px solid #4CAF50; padding: 20px; border-radius: 10px; text-align: center;">
                <h1 style="color: #4CAF50;">{st.session_state.result:.2f} {to_unit}</h1>
            </div>
        """, unsafe_allow_html=True)

# History feature
if 'history' not in st.session_state:
    st.session_state.history = []

if st.button("Save to History"):
    if st.session_state.result is not None:
        st.session_state.history.append((f"{value:.2f}", from_unit, f"{st.session_state.result:.2f}", to_unit))
        st.success("Conversion saved to history!")
        
        # Add congratulations effect
        st.components.v1.html("""
            <script>
                function showConfetti() {
                    var confettiSettings = { target: 'my-canvas' };
                    var confetti = new ConfettiGenerator(confettiSettings);
                    confetti.render();
                }
                showConfetti();
            </script>
            <canvas id="my-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;"></canvas>
            <script src="https://cdn.jsdelivr.net/npm/confetti-js@0.0.18/dist/index.min.js"></script>
        """, height=0)
    else:
        st.error("Please perform a conversion first.")

# Display conversion history
if st.session_state.history:
    st.subheader("Conversion History")
    conversion_history(st.session_state.history)