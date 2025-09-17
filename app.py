import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🌱 Recomendación de Cultivos - Análisis Exploratorio")

# ==============================
# 1. Cargar dataset
# ==============================
@st.cache_data
def load_data():
    return pd.read_csv("Crop_recommendation.csv")

df = load_data()

# ==============================
# 2. Vista previa y estadísticas
# ==============================
st.subheader("📋 Vista previa del dataset")
st.dataframe(df.head())

if st.checkbox("Mostrar estadísticas descriptivas"):
    st.write(df.describe())

# ==============================
# 3. Histograma interactivo
# ==============================
st.subheader("📊 Histograma interactivo")
columna = st.sidebar.selectbox("Selecciona variable numérica", df.select_dtypes(include="number").columns)

fig, ax = plt.subplots()
sns.histplot(df[columna], kde=True, ax=ax)
st.pyplot(fig)

# ==============================
# 4. Scatter plot interactivo
# ==============================
st.subheader("🔍 Relación entre variables (Scatter)")
x_var = st.sidebar.selectbox("Eje X", df.select_dtypes(include="number").columns)
y_var = st.sidebar.selectbox("Eje Y", df.select_dtypes(include="number").columns)

fig, ax = plt.subplots()
sns.scatterplot(x=df[x_var], y=df[y_var], ax=ax)
st.pyplot(fig)

# ==============================
# 5. Heatmap de correlación
# ==============================
st.subheader("🔥 Matriz de correlación")
fig, ax = plt.subplots(figsize=(10,6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# ==============================
# 6. Promedios por cultivo
# ==============================
st.subheader("🌾 Promedio de N, P, K por cultivo")
promedios = df.groupby("label")[["N", "P", "K"]].mean()
st.dataframe(promedios)
