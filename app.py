import streamlit as st
from database import init_db, insert_record, load_records
from ai_engine import train_ai
from analytics import create_dataframe
from ancestral_knowledge import knowledge
from natural_cycles import moon_phase, time_of_day
from community_insights import community_message

init_db()

st.title("🌊 Ancestral Ocean Intelligence")
st.write("Explorando la relación entre naturaleza y bienestar humano")

st.subheader("Ciclos naturales")
st.write("Fase lunar:", moon_phase())
st.write("Momento del día:", time_of_day())

st.subheader("Registra tu día")
energy = st.slider("energía",1,10)
mood = st.slider("estado de ánimo",1,10)
stress = st.slider("estrés",1,10)
sleep = st.slider("horas sueño",0,12)
nature = st.slider("tiempo en naturaleza",0,10)
surf = st.slider("surf",0,5)
fishing = st.slider("pesca",0,8)
cannabis = st.slider("cannabis",0,5)
food = st.slider("calidad comida",1,10)
notes = st.text_area("reflexiones")

if st.button("guardar día"):
    insert_record((energy,mood,stress,sleep,nature,surf,fishing,cannabis,food,notes))
    st.success("registro guardado")

rows = load_records()
if rows:
    df = create_dataframe(rows)
    st.subheader("evolución energía")
    st.line_chart(df["energy"])

    st.subheader("recomendaciones")
    rec=[]
    if energy<4:
        rec += knowledge["rest"]
    if stress>7:
        rec += knowledge["balance"]
    if energy>7:
        rec += knowledge["energy"]
    if mood>7:
        rec += knowledge["creativity"]
    rec = list(set(rec))
    for r in rec:
        st.write("•", r)

    st.subheader("aprendizaje IA")
    model = train_ai(df)
    if model:
        pred = model.predict([[sleep,nature,surf,fishing,cannabis,food]])
        st.write("predicción energía futura:", round(pred[0],2))

st.subheader("comunidad")
st.write(community_message())
from reflection_engine import generate_reflection
from community_analysis import community_insights

if rows:
    df = create_dataframe(rows)

    st.subheader("Reflexión personal del día")
    today_record = {
        "energy": energy,
        "mood": mood,
        "stress": stress,
        "sleep": sleep,
        "nature": nature,
        "surf": surf,
        "fishing": fishing,
        "cannabis": cannabis,
        "food": food
    }

    reflection_text = generate_reflection(today_record, df)
    st.write(reflection_text)

    st.subheader("Insights de la comunidad")
    community_text = community_insights(df)  # por ahora tus propios registros, luego puede ser global
    st.write(community_text)
