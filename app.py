import streamlit as st

# FUNCTIONS
def distance_converter(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5 / 9
    else:
        return value

def weight_converter(from_unit, to_unit, value):
    units = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
    }
    return value * units[from_unit] / units[to_unit]

def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascal": 1,
        "Bar": 100000,
        "PSI": 6894.76,
        "Atmosphere": 101325,
    }
    return value * units[from_unit] / units[to_unit]

# UI
st.title("🧮 Universal Unit Converter")

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])
value = st.number_input("Enter Value", format="%.4f")

if category == "Distance":
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
    if st.button("Convert"):
        result = distance_converter(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    if st.button("Convert"):
        result = temperature_converter(from_unit, to_unit, value)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", ["Kilogram", "Gram", "Pound", "Ounce"])
    to_unit = st.selectbox("To", ["Kilogram", "Gram", "Pound", "Ounce"])
    if st.button("Convert"):
        result = weight_converter(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Pressure":
    from_unit = st.selectbox("From", ["Pascal", "Bar", "PSI", "Atmosphere"])
    to_unit = st.selectbox("To", ["Pascal", "Bar", "PSI", "Atmosphere"])
    if st.button("Convert"):
        result = pressure_converter(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
