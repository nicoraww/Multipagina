# page_A.py
import streamlit as st
import random

st.title("📄 Página A")
st.markdown("**Palabras que empiezan con A**")

# Lista de ejemplos
words_a = [
    "Árbol", "Amigo", "Avión", "Agua",
    "Arco", "Arte", "Arena", "Auto",
    "Abrazo", "Aire"
]

if st.button("🎲 Mostrar palabra aleatoria con A"):
    choice = random.choice(words_a)
    st.success(f"**{choice}**")

st.write("Lista completa:")
st.write(words_a)

