import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================
# Título y descripción
# ==========================
st.title("🌱 Análisis Exploratorio - Crop Recommendation Dataset")
st.write("""
Esta aplicación interactiva permite explorar el **Crop Recommendation Dataset**.  
Podrás visualizar distribuciones, correlaciones y relaciones entre variables del suelo y clima.
""")

# ==========================
# Cargar dataset
# ==========================
@st.cache_data
def load_data():
    return pd.read_csv("Crop_recommendation.csv")

df = load_data()

st.subheader("Vista previa de los datos")
st.dataframe(df.head())

# ==========================
# Estadísticas básicas
# ==========================
if st.checkbox("Mostrar estadísticas descriptivas"):
    st.write(df.describe())

# ==========================
# Histograma interactivo
# ==========================
st.subheader("📊 Histograma")
columna = st.sidebar.selectbox("Selecciona una variable numérica", df.select_dtypes(include="number").columns)

fig, ax = plt.subplots()
sns.histplot(df[columna], kde=True, ax=ax)
st.pyplot(fig)

# ==========================
# Scatter plot interactivo
# ==========================
st.subheader("🔍 Relación entre variables")
x_var = st.sidebar.selectbox("Variable en eje X", df.select_dtypes(include="number").columns)
y_var = st.sidebar.selectbox("Variable en eje Y", df.select_dtypes(include="number").columns)

fig, ax = plt.subplots()
sns.scatterplot(x=df[x_var], y=df[y_var], ax=ax)
st.pyplot(fig)

# ==========================
# Heatmap de correlación
# ==========================
st.subheader("🔥 Matriz de correlación")
corr = df.select_dtypes(include="number").corr()
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# ==========================
# Agrupación por cultivo
# ==========================
st.subheader("🌾 Promedio de N, P, K por cultivo")
promedios = df.groupby("label")[["N","P","K"]].mean()
st.dataframe(promedios)
