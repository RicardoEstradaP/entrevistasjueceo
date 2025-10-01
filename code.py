import streamlit as st
import math

def calcular_jueces(num_aspirantes: int, 
                    carga_deseada: int = 12, 
                    porcentaje_discrepancias: float = 0.2):
    """
    Calcula jueces necesarios considerando 2 por aspirante + árbitro en discrepancias.
    """
    # Entrevistas base
    entrevistas_base = num_aspirantes * 2
    
    # Entrevistas extra por discrepancias
    entrevistas_extra = int(num_aspirantes * porcentaje_discrepancias)
    
    # Total de entrevistas
    total_entrevistas = entrevistas_base + entrevistas_extra
    
    # Número recomendado de jueces
    jueces_necesarios = math.ceil(total_entrevistas / carga_deseada)
    
    # Carga real
    carga_real = total_entrevistas / jueces_necesarios
    
    return entrevistas_base, entrevistas_extra, total_entrevistas, jueces_necesarios, carga_real


# -----------------------------
# Dashboard en Streamlit
# -----------------------------
st.set_page_config(page_title="Cálculo de jueces con árbitro", layout="centered")

st.title("⚖️ Cálculo de jueces: 2 por aspirante + árbitro en discrepancias")

num_aspirantes = st.number_input("Número de aspirantes", min_value=1, value=50, step=1)
carga_deseada = st.slider("Carga deseada por juez (entrevistas)", 5, 20, 12)
porcentaje_discrepancias = st.slider("Proporción estimada de discrepancias (%)", 0, 100, 20) / 100

entrevistas_base, entrevistas_extra, total_entrevistas, jueces_necesarios, carga_real = calcular_jueces(
    num_aspirantes, carga_deseada, porcentaje_discrepancias
)

st.subheader("📊 Resultados")
st.metric("Entrevistas base (2 por aspirante)", entrevistas_base)
st.metric("Entrevistas extra (árbitro)", entrevistas_extra)
st.metric("Total de entrevistas", total_entrevistas)
st.metric("Jueces necesarios (aprox.)", jueces_necesarios)
st.metric("Carga real por juez", f"{carga_real:.1f}")

st.info("""
Este cálculo asume **2 jueces por aspirante** como base, 
y añade un **tercer juez solo en casos de discrepancias**.
""")
