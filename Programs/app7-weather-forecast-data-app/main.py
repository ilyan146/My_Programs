import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")

days = st.slider("Forecasted Days", min_value=1, max_value=5)

option = st.selectbox("Select data to view",("Temperature","Sky"))

st.subheader(f"{option} for the next {days} days in {place}")
try:
    if place:

        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [i["main"]["temp"]/10 for i in filtered_data]
            dates = [i["dt_txt"] for i in filtered_data]
            figure = px.line(x=dates,y=temperatures, labels={"x":"Dates", "y":"Temperature (C)"})
            st.plotly_chart(figure)

        elif option == "Sky":
            sky_conditions = [i["weather"][0]["main"] for i in filtered_data]
            images = {"Clear": "004 images/clear.png", "Clouds":"004 images/cloud.png",
                      "Rain": "004 images/rain.png", "Snow": "004 images/snow.png"}
            image_paths = [images[i] for i in sky_conditions]
            st.image(image_paths, width=115)
except KeyError:
    st.info("That place does not exist, please input a correct place, thank you!")


