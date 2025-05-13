import streamlit as st
import pickle

st.title("Weather Prediction App..")
pn=st.number_input("Enter precipitation")
maxt=st.number_input("Enter maximum temperature")
mint=st.number_input("Enter minimum temperature")
wind=st.number_input("ENter the wind speed")
button=st.button("predict!")
if button:
    if mint > maxt:
        st.error("❌ Minimum temperature cannot be greater than maximum temperature.")
    else:
        lr=pickle.load(open("wp.pkl","rb"))    #open our weather prediction model which will be open in rb format means REad Binary.
        res=lr.predict([[pn,maxt,mint,wind]])[0]
        emoji = {
            "Sunny": "☀️",
            "Rainy": "🌧️",
            "Cloudy": "☁️",
            "Storm": "⛈️"
        }
        st.markdown(f"Today weather situation : {res}")


