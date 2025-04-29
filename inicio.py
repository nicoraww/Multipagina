# page_O.py
import streamlit as st
import random

st.title("📄 Página O")
st.markdown("**Palabras que empiezan con O**")

# Lista de ejemplos
words_o = [
    "Oso", "Olla", "Oro", "Oveja",
    "Olivo", "Oído", "Otoño", "Ópera",
    "Orgullo", "Orquesta"
]

if st.button("🎲 Mostrar palabra aleatoria con O"):
    choice = random.choice(words_o)
    st.success(f"**{choice}**")

st.write("Lista completa:")
st.write(words_o)
