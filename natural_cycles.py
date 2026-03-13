from datetime import datetime

def moon_phase():
    day = datetime.now().day
    if day <= 7:
        return "luna creciente"
    elif day <= 14:
        return "luna llena"
    elif day <= 21:
        return "luna menguante"
    else:
        return "luna nueva"

def time_of_day():
    hour = datetime.now().hour
    if hour < 12:
        return "mañana"
    elif hour < 18:
        return "tarde"
    else:
        return "noche"
