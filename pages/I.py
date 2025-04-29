# page_I.py
import streamlit as st
import random

st.title("📄 Página I")
st.markdown("**Palabras que empiezan con I**")

# Lista de ejemplos
words_i = [
    "Isla", "Iglesia", "Invierno", "Idioma",
    "Idea", "Ídolo", "Imagen", "Índice",
    "Intenso", "Irradiar"
]

if st.button("🎲 Mostrar palabra aleatoria con I"):
    choice = random.choice(words_i)
    st.success(f"**{choice}**")

st.write("Lista completa:")
st.write(words_i)

