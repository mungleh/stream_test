import streamlit as st
import pandas as pd
import requests
import json
import gmaps
from ipywidgets import embed
import streamlit.components.v1 as components
import pydeck as pdk

#CSS pour la classe
st.set_page_config(
    page_title="Main page",
    layout="wide"
)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

#clé api dans le .streamlit/secrets.toml
key = st.secrets["API_KEY"]

st.title("Find Ville")

#data villes de france
def get_ville():
    data = pd.read_csv("pages/cities.csv", delimiter = ",")
    data = data[['city_code']]
    data = data.drop_duplicates()
    return data

#sélection de la ville
def select_ville():
    ville = st.selectbox('', get_ville())
    return ville

selected_ville = select_ville()

col1, col2 = st.columns(2)

#la ou la température doit aller mais sa marche pas, faudrait faire un session state pour temp vu qu'on le recup plus tard tavu pelow
with col1:
    try:
        st.markdown(f'<p style="font-family:sans-serif; font-size: 42px;">{temp}°C</p>', unsafe_allow_html=True)
    except:
        st.markdown(f'<p style="font-family:sans-serif; font-size: 42px;">20°C</p>', unsafe_allow_html=True)

#bouton pour avoir la localisation
with col2:
    predict = st.button("Prédire")

    if predict:
        #encoder les espace pour l'url
        select_encoded = selected_ville.replace(" ", "%20")
        #requète pour avoir la loc de la ville
        get_loc = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={select_encoded},FRA&limit=1&appid={key}').json()
        lat = get_loc[0]["lat"]
        lon = get_loc[0]["lon"]
        #requète pour avoir les info dla ville
        use_loc = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}').json()
        temp = use_loc['main']['temp']

#carte
try:
    st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=lat,
        longitude=lon,
        zoom=10
    )))

except:
    st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=46.22,
        longitude=2.21,
        zoom=6
    )))
