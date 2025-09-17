# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🌱 Recomendación de Cultivos - Análisis Estadístico")

# ==============================
# 1. Cargar dataset
# ==============================
@st.cache_data
def load_data():
    # El archivo debe estar en la misma carpeta del repo
    return pd.read_csv("Crop_recommendation.csv")

df = load_data()

st.subheader("Vista previa del dataset")
st.dataframe(df.head())

# ==============================
# 2. Estadísticas descriptivas
# ==============================
st.subheader("Estadísticas descriptivas")
st.write(df.describe())

# ==============================
# 3. Heatmap de correlación
# ==============================
st.subheader("Mapa de correlación entre variables")
plt.figure(figsize=(10, 6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
st.pyplot(plt)

# ==============================
# 4. Promedios de N, P, K por cultivo
# ==============================
st.subheader("Promedio de N, P, K por cultivo")
promedios = df.groupby("label")[["N", "P", "K"]].mean()
st.dataframe(promedios)
