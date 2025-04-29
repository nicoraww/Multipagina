# page_U.py
import streamlit as st
import random

st.title("📄 Página U")
st.markdown("**Palabras que empiezan con U**")

# Lista de ejemplos
words_u = [
    "Uva", "Uña", "Útil", "Ubicación",
    "Último", "Universo", "Unicornio",
    "Unión", "Urgente", "Unidad"
]

if st.button("🎲 Mostrar palabra aleatoria con U"):
    choice = random.choice(words_u)
    st.success(f"**{choice}**")

st.write("Lista completa:")
st.write(words_u)
