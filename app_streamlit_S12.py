# Import des modules nécessaires :

import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import streamlit_option_menu as som
import yaml
from yaml.loader import SafeLoader

# Import des données comptes en CSV (soit CSV, soit YAML)
# df_comptes = pd.read_csv('C:\Users\vieas\Documents\GitHub\streamlit\donnees_comptes.csv')


# Chargement des données depuis un fichier YAML pour la configuration
with open('configuration.yaml') as file: # Il faut s'assurer que le fichier est dans le même dossier
    config = yaml.load(file, Loader=SafeLoader)

# Initialisation de l'authentificateur
authenticator = stauth.Authenticate(
    config['credentials'],            # Les identifiants et mots de passe
    config['cookie']['name'],         # Nom du cookie
    config['cookie']['key'],          # Clé de sécurisation du cookie
    config['cookie']['expiry_days']   # Durée d'expiration en jours
)


# Gestion de la connexion
name, authentication_status, username = authenticator.login("Login", "main")


# Gestion des pages après connexion
def accueil():
    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")

if authentication_status:
    # Page d'accueil après connexion réussie
    accueil()
    # Ajout d'un bouton de déconnexion
    authenticator.logout("Déconnexion", "sidebar")

elif authentication_status is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect.")
elif authentication_status is None:
    st.warning("Veuillez entrer vos identifiants.")

# Création du menu pour la navigation
if authentication_status:
    selection = som.option_menu(
        menu_title=None,
        options=["Accueil", "Photos"]
    )

    # Navigation entre les pages
    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Un chat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("Un chien")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.header("Un hibou")
            st.image("https://static.streamlit.io/examples/owl.jpg")