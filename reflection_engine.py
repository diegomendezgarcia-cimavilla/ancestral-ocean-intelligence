from ancestral_knowledge import knowledge

def generate_reflection(record, df=None):
    """
    Genera una reflexión narrativa basada en los datos del día y patrones históricos.
    record: dict con claves energy,mood,stress,sleep,nature,surf,fishing,cannabis,food
    df: dataframe histórico opcional para comparación
    """
    reflection = []

    # Conexión con la naturaleza
    if record["nature"] >= 7:
        reflection.append("Hoy pasaste mucho tiempo en contacto con la naturaleza, esto suele aumentar la claridad mental y reducir el estrés.")
    elif record["nature"] <= 3:
        reflection.append("Podrías beneficiarte de pasar más tiempo al aire libre para equilibrar tu energía y ánimo.")

    # Sueño
    if record["sleep"] < 6:
        reflection.append("Dormir pocas horas puede afectar tu energía y concentración, considera descansar más mañana.")
    elif record["sleep"] >= 8:
        reflection.append("Tu descanso fue suficiente; esto probablemente contribuyó a mantener tu energía estable.")

    # Surf y pesca
    if record["surf"] > 0:
        reflection.append("El surf te ayuda a liberar estrés y mantener el cuerpo activo; es una buena práctica diaria.")
    if record["fishing"] > 4:
        reflection.append("Pasar muchas horas pescando puede ser relajante, pero cuidado con la fatiga física.")

    # Cannabis
    if record["cannabis"] > 3:
        reflection.append("El consumo alto de cannabis puede influir en tu energía y concentración; observa cómo te afecta.")

    # Energía y ánimo
    if record["energy"] < 5:
        reflection.append("Tu energía hoy fue baja; combina descanso y contacto con naturaleza para recargar.")
    if record["mood"] < 5:
        reflection.append("Tu ánimo estuvo bajo; actividades creativas o reflexivas pueden ayudarte a equilibrarlo.")

    # Comparaciones históricas
    if df is not None and len(df) > 10:
        mean_energy = df["energy"].mean()
        if record["energy"] > mean_energy:
            reflection.append("Tu energía hoy está por encima del promedio, excelente progreso.")
        else:
            reflection.append("Comparado con tus días anteriores, hoy tu energía fue menor; reflexiona sobre posibles causas.")

    return "\n".join(reflection)
