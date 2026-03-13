import pandas as pd

def create_dataframe(rows):
    columns=["date","energy","mood","stress","sleep","nature","surf","fishing","cannabis","food","notes"]
    return pd.DataFrame(rows,columns=columns)
