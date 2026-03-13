def community_insights(df):
    """
    Genera insights basados en datos históricos de la comunidad.
    df: dataframe con registros históricos de todos los usuarios (anónimos)
    """
    insights = []

    if df is None or len(df) < 5:
        return "No hay suficientes datos de comunidad para generar insights."

    # Ejemplo simple: promedio energía vs tiempo en naturaleza
    avg_energy = df["energy"].mean()
    avg_nature = df["nature"].mean()
    insights.append(f"En la comunidad, quienes pasan más tiempo en la naturaleza ({avg_nature:.1f} sobre 10) suelen tener una energía promedio de {avg_energy:.1f}.")

    avg_sleep = df["sleep"].mean()
    insights.append(f"Promedio de sueño en la comunidad: {avg_sleep:.1f}h. Dormir bien correlaciona con mejor ánimo y energía.")

    return "\n".join(insights)
