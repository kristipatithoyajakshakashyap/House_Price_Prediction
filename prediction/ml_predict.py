import numpy as np
import pickle
import pandas as pd 

house = pd.read_csv('F:/kavyamini/mini/prediction/house_price.csv')
def predict_price(location, sqft, bath, bhk):
    x = house.drop('price', axis=1)
    loc_index = np.where(x.columns == location)[0][0]

    X = np.zeros(len(x.columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_index >= 0:
        X[loc_index] = 1
    lr = pickle.load(open('F:/kavyamini/mini/prediction/house_model.sav', 'rb'))
    prediction = lr.predict([X])[0]
    return prediction
