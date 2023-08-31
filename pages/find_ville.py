import streamlit as st
import requests
import streamlit.components.v1 as components
import pydeck as pdk

# Mise en forme CSS pour la page
st.set_page_config(
    page_title="Page principale",
    layout="wide"
)

# Clé API d'OpenWeather
# key = st.secrets("API_KEY")
key = "f325ed9d2480dfc6a881b7ecb48c311d"
# Fonction pour obtenir la localisation d'une ville
@st.cache_data
def get_ville_loc(ville):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={ville}&appid={key}"
    response = requests.get(url)
    if response.status_code == 200:
        ville_json = response.json()
        return ville_json

# Mise en forme CSS pour un conteneur
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

# Titre de la page
st.title("Trouver une Ville")

# Zone de saisie pour la ville
ville_dropdown = st.text_input("Saisissez le nom d'une ville")

# Création de deux colonnes pour affichage
col1, col2 = st.columns(2)

# Bouton pour prédire
with col2:
    predict = st.button("Prédire")

    if predict:
        try :
            # Obtention de la localisation de la ville
            loc_ville = get_ville_loc(ville_dropdown)
            lat = loc_ville[0]["lat"]
            lon = loc_ville[0]["lon"]
            # Requête pour obtenir les informations météo de la ville
            info_meteo = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}').json()
            temp = info_meteo['main']['temp']
        except :
            st.markdown("Ville introuvable ou erreur de saisie")
# Affichage de la température
with col1:
    try:
        st.markdown(f'<p style="font-family:sans-serif; font-size: 42px;">{temp}°C</p>', unsafe_allow_html=True)
    except:
        st.markdown(f'En attente de prédiction')

# Affichage de la carte
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
