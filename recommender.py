import pandas as pd
from sklearn.neighbors import NearestNeighbors

data = pd.read_csv('skincare_data.csv')
features = data[['Oily', 'Dry', 'Acne', 'Pigmentation']]
model = NearestNeighbors(n_neighbors=3)
model.fit(features)

def get_recommendations(user_input):
    distances, indices = model.kneighbors([user_input])
    recommendations = []
    for i in indices[0]:
        recommendations.append({
            'Name': data.iloc[i]['Name'],
            'Ingredients': data.iloc[i]['Ingredients']
        })
    return recommendations
