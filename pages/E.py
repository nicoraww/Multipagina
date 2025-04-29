# page_E.py
import streamlit as st
import random

st.title("📄 Página E")
st.markdown("**Palabras que empiezan con E**")

# Lista de ejemplos
words_e = [
    "Elefante", "Escuela", "Espada", "Estrella",
    "Esperanza", "Energía", "Entrada", "Equipo",
    "Ejemplo", "Etiqueta"
]

if st.button("🎲 Mostrar palabra aleatoria con E"):
    choice = random.choice(words_e)
    st.success(f"**{choice}**")

st.write("Lista completa:")
st.write(words_e)

