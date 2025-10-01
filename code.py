import streamlit as st
import math

# -----------------------------
# Función para calcular jueces
# -----------------------------
def calcular_jueces(num_aspirantes: int, entrevistas_por_aspirante: int = 2, carga_deseada: int = 12):
    """
    Calcula el número recomendado de jueces.
    - num_aspirantes: número de aspirantes (N)
    - entrevistas_por_aspirante: jueces por aspirante (k)
    - carga_deseada: entrevistas aproximadas que se busca por juez
    """
    total_entrevistas = num_aspirantes * entrevistas_por_aspirante
    jueces_necesarios = math.ceil(total_entrevistas / carga_deseada)
    carga_real = total_entrevistas / jueces_necesarios
    return total_entrevistas, jueces_necesarios, carga_real


# -----------------------------
# Dashboard en Streamlit
# -----------------------------
st.set_page_config(page_title="Cálculo de jueces para entrevistas", layout="centered")

st.title("📊 Cálculo de jueces para entrevistas de admisión")

st.markdown("""
Este dashboard ayuda a estimar **cuántos jueces** necesitas para entrevistar a tus aspirantes.  
Se basa en tres parámetros:  
1. Número de aspirantes  
2. Entrevistas por aspirante (jueces asignados a cada candidato)  
3. Carga deseada de entrevistas por juez
""")

# Entrada de usuario
num_aspirantes = st.number_input("Número de aspirantes", min_value=1, value=50, step=1)
entrevistas_por_aspirante = st.slider("Entrevistas por aspirante (k)", 1, 5, 2)
carga_deseada = st.slider("Carga deseada por juez (entrevistas)", 5, 20, 12)

# Cálculo
total_entrevistas, jueces_necesarios, carga_real = calcular_jueces(
    num_aspirantes, entrevistas_por_aspirante, carga_deseada
)

# Resultados
st.subheader("📈 Resultados")
st.metric("Total de entrevistas requeridas", total_entrevistas)
st.metric("Jueces necesarios (aprox.)", jueces_necesarios)
st.metric("Carga real por juez", f"{carga_real:.1f}")

# Recomendaciones
st.subheader("✅ Recomendaciones")
st.markdown(f"""
- Para **{num_aspirantes} aspirantes** y **{entrevistas_por_aspirante} jueces por aspirante**, 
  se requieren **{total_entrevistas} entrevistas en total**.  
- Con una carga deseada de **{carga_deseada} entrevistas por juez**, 
  necesitas **{jueces_necesarios} jueces**.  
- La carga real promedio será de **{carga_real:.1f} entrevistas por juez**.
""")

st.info("Tip: Puedes ajustar el número de entrevistas por aspirante (k) y la carga deseada para simular distintos escenarios.")
