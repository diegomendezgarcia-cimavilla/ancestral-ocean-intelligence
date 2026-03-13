import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def train_ai(df):
    if len(df) < 20:
        return None
    X = df[["sleep","nature","surf","fishing","cannabis","food"]]
    y = df["energy"]
    model = RandomForestRegressor()
    model.fit(X, y)
    return model
