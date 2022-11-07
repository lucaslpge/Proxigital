import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide", page_title='Analyse Proxigital', page_icon=':computer:')


# ------------------------------------------------ CHARGER CSV ------------------------------------------------ #


def load_csv():
    df = pd.read_csv('transactions.csv')
    df
    return df


# ------------------------------------------------ FONCTIONS ------------------------------------------------ #


def aff_meilleures_bornes(df):
    st.subheader("100 bornes qui ont fait le plus de ventes cette année :")
    st.write(df['Organisation'].value_counts())

def aff_meilleurs_jours(df):
    st.subheader("Jours meilleurs ventes :")
    tab1, tab2 = st.tabs(["🥇 Classement", "📈 Graphique"])
    with tab1:
        st.write(df['jour'].value_counts())
    with tab2:
        hist_values = np.histogram(df.jour, bins=31, range=(1, 31))[0]
        st.bar_chart(hist_values)

def aff_meilleurs_mois(df):
    st.subheader("Mois meilleures ventes :")
    tab1, tab2 = st.tabs(["🥇 Classement", "📈 Graphique"])
    with tab1:
        st.write(df['mois'].value_counts())
    with tab2:
        hist_values = np.histogram(df.mois, bins=12, range=(1, 12))[0]
        st.bar_chart(hist_values)

def aff_meilleures_heures(df):
    st.subheader("Heures meilleures ventes :")
    tab1, tab2 = st.tabs(["🥇 Classement", "📈 Graphique"])
    with tab1:
        st.write(df['Heure precise'].value_counts())
    with tab2:
        hist_values = np.histogram(df['Heure precise'], bins=24, range=(0, 23))[0]
        st.bar_chart(hist_values)


def aff_meilleurs_services(df):
    left_col, right_col = st.columns(2)
    with left_col:
        st.subheader("Meilleurs services :")
        st.write(df['Service'].value_counts())
    with right_col:
        st.subheader("Meilleurs sous-services :")
        st.write(df['Sous-service'].value_counts())


def statut_de_paiement(df):
    st.subheader("Statut de paiement :")
    st.write(df['Statut de paiement'].value_counts())


# ------------------------------------------------ MAIN ------------------------------------------------ #


def main():
    df = load_csv()
    aff_meilleures_bornes(df)
    aff_meilleurs_jours(df)
    aff_meilleurs_mois(df)
    aff_meilleures_heures(df)
    aff_meilleurs_services(df)
    statut_de_paiement(df)

main()


'''
    Google FORM : 
        - où la borne est placée dans la boutique
        - à côté de quoi? (tabac, magazines, journaux...)
        - à combien ils évaluent le fait qu'il la mette en avant aux clients (note de 1 à 10)
        - des clients qui viennent que pour ça ?
        - clients besoin d'aide ou non ? et si oui sur quels services ?
        - moyen d'âge des clients qui l'utilisent  
'''